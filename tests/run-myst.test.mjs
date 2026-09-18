import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';

import { createNpmVersionShim, npmVersion, realNpmPath } from '../scripts/run-myst.mjs';

test('npmVersion prefers the npm process user agent', () => {
  assert.equal(npmVersion({ npm_config_user_agent: 'npm/10.9.8 node/v22.22.3 linux x64' }), '10.9.8');
});

test('npmVersion falls back to the pinned package manager', () => {
  assert.equal(npmVersion({}), '10.9.8');
});

test('realNpmPath prefers the executable used by the current npm process', () => {
  assert.equal(realNpmPath({ npm_execpath: process.execPath }), process.execPath);
});

test('npm version shim exposes the selected version on POSIX and Windows', () => {
  const shimDir = createNpmVersionShim('10.9.8');

  try {
    assert.match(fs.readFileSync(path.join(shimDir, 'npm'), 'utf8'), /printf .*10\.9\.8/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm'), 'utf8'), /exec "\$MYST_REAL_NPM"/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm.cmd'), 'utf8'), /echo 10\.9\.8/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm.cmd'), 'utf8'), /MYST_REAL_NPM/);
    assert.equal(fs.statSync(path.join(shimDir, 'npm')).mode & 0o111, 0o111);
  } finally {
    fs.rmSync(shimDir, { recursive: true, force: true });
  }
});
