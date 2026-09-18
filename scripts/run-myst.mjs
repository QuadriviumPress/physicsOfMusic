#!/usr/bin/env node

/**
 * Run the local MyST CLI with a reliable `npm --version` probe.
 *
 * MyST 1.10.1 bundles check-node-version, which launches `npm --version` from
 * Node and captures stdout. Some Node/npm environments return status 0 but an
 * empty stdout for that nested probe, so MyST reports "npm Package Not Found"
 * and exits before doing any work. The project toolchain check still validates
 * the real npm executable; this launcher only gives MyST's broken probe the
 * same version that npm exposed to the current npm script.
 */

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const scriptPath = fileURLToPath(import.meta.url);
const root = path.resolve(path.dirname(scriptPath), '..');

export function npmVersion(env = process.env, packageJsonPath = path.join(root, 'package.json')) {
  const agentMatch = /(?:^|\s)npm\/(\d+(?:\.\d+){0,2})(?:\s|$)/.exec(env.npm_config_user_agent ?? '');
  if (agentMatch) return agentMatch[1];

  const { packageManager = '' } = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
  const declaredMatch = /^npm@(\d+(?:\.\d+){0,2})$/.exec(packageManager);
  if (declaredMatch) return declaredMatch[1];

  throw new Error('Unable to determine npm version from npm_config_user_agent or packageManager.');
}

export function createNpmVersionShim(version) {
  const shimDir = fs.mkdtempSync(path.join(os.tmpdir(), 'myst-npm-'));
  const posixShim = path.join(shimDir, 'npm');
  const windowsShim = path.join(shimDir, 'npm.cmd');

  fs.writeFileSync(
    posixShim,
    `#!/bin/sh\nif [ "$1" = "--version" ]; then\n  printf '%s\\n' '${version}'\n  exit 0\nfi\nexec "$MYST_REAL_NPM" "$@"\n`,
  );
  fs.chmodSync(posixShim, 0o755);
  fs.writeFileSync(
    windowsShim,
    `@echo off\r\nif "%~1"=="--version" (\r\n  echo ${version}\r\n  exit /b 0\r\n)\r\nif /i "%MYST_REAL_NPM:~-3%"==".js" (\r\n  node "%MYST_REAL_NPM%" %*\r\n) else (\r\n  "%MYST_REAL_NPM%" %*\r\n)\r\n`,
  );

  return shimDir;
}

export function realNpmPath(env = process.env) {
  if (env.npm_execpath && fs.existsSync(env.npm_execpath)) return env.npm_execpath;

  const names = process.platform === 'win32' ? ['npm.cmd', 'npm.exe', 'npm'] : ['npm'];
  for (const directory of (env.PATH ?? '').split(path.delimiter)) {
    for (const name of names) {
      const candidate = path.join(directory, name);
      if (fs.existsSync(candidate)) return candidate;
    }
  }

  throw new Error('Unable to locate the real npm executable.');
}

export function runMyst(args, env = process.env) {
  const version = npmVersion(env);
  const npmPath = realNpmPath(env);
  const shimDir = createNpmVersionShim(version);
  const mystBin = path.join(root, 'node_modules', '.bin', process.platform === 'win32' ? 'myst.cmd' : 'myst');

  try {
    const result = spawnSync(mystBin, args, {
      cwd: process.cwd(),
      env: {
        ...env,
        MYST_REAL_NPM: npmPath,
        PATH: `${shimDir}${path.delimiter}${env.PATH ?? ''}`,
      },
      stdio: 'inherit',
    });

    if (result.error) throw result.error;
    return result.status ?? 1;
  } finally {
    fs.rmSync(shimDir, { recursive: true, force: true });
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === scriptPath) {
  process.exitCode = runMyst(process.argv.slice(2));
}
