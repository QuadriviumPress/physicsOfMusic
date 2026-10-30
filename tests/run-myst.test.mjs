import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';

import { createNpmVersionShim, npmVersion, realNpmPath } from '../scripts/run-myst.mjs';

test('npmVersion prefers the npm process user agent', () => {
  assert.equal(npmVersion({ npm_config_user_agent: 'npm/11.20.0 node/v26.0.0 linux x64' }), '11.20.0');
});

test('npmVersion falls back to the pinned package manager', () => {
  assert.equal(npmVersion({}), '11.20.0');
});

test('realNpmPath prefers the executable used by the current npm process', () => {
  assert.equal(realNpmPath({ npm_execpath: process.execPath }), process.execPath);
});

test('npm version shim exposes the selected version on POSIX and Windows', () => {
  const shimDir = createNpmVersionShim('11.20.0');

  try {
    assert.match(fs.readFileSync(path.join(shimDir, 'npm'), 'utf8'), /printf .*11\.20\.0/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm'), 'utf8'), /exec "\$MYST_REAL_NPM"/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm.cmd'), 'utf8'), /echo 11\.20\.0/);
    assert.match(fs.readFileSync(path.join(shimDir, 'npm.cmd'), 'utf8'), /MYST_REAL_NPM/);
    assert.equal(fs.statSync(path.join(shimDir, 'npm')).mode & 0o111, 0o111);
  } finally {
    fs.rmSync(shimDir, { recursive: true, force: true });
  }
});
