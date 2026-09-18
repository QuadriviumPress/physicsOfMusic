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
            script = root / "scripts/build-exports.sh"
            shutil.copy(Path(__file__).resolve().parents[1] / "scripts/build-exports.sh", script)
            launcher = root / "scripts/run-myst.mjs"
            launcher.write_text(
                "import fs from 'node:fs';\n"
                "fs.mkdirSync('exports', { recursive: true });\n"
                "fs.writeFileSync('exports/physics-of-music.pdf', 'PDF fixture');\n"
            )
            result = subprocess.run(["bash", str(script), "pdf"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(
                {file.name for file in (root / "exports").iterdir()},
                {"physics-of-music.pdf", "physics-of-music-student.pdf"},
            )
            self.assertIn("physics-of-music-student.pdf", result.stdout)
            launcher.write_text("process.exit(17);\n")
            result = subprocess.run(["bash", str(script), "pdf"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 17)
