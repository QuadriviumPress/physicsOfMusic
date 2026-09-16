import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class BuildExportsTests(unittest.TestCase):
    def test_pdf_only_build_succeeds_without_docx_and_preserves_build_failures(self):
        with tempfile.TemporaryDirectory(prefix="physics-export-script-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            (root / "bin").mkdir()
            script = root / "scripts/build-exports.sh"
            shutil.copy(Path(__file__).resolve().parents[1] / "scripts/build-exports.sh", script)
            npx = root / "bin/npx"
            npx.write_text("#!/bin/sh\nmkdir -p exports\nprintf 'PDF fixture' > exports/physics-of-music.pdf\n")
            npx.chmod(0o755)
            env = {**os.environ, "PATH": f"{root / 'bin'}:{os.environ['PATH']}"}
            result = subprocess.run(["bash", str(script), "pdf"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(
                {file.name for file in (root / "exports").iterdir()},
                {"physics-of-music.pdf", "physics-of-music-student.pdf"},
            )
            self.assertIn("physics-of-music-student.pdf", result.stdout)
            npx.write_text("#!/bin/sh\nexit 17\n")
            result = subprocess.run(["bash", str(script), "pdf"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 17)
