import os
import sys
import shlex
import shutil
import contextlib
import subprocess

from iface import AbstractCommandExecutor


class FunctionalTestRunner(AbstractCommandExecutor):
    def __init__(self, start_path):
        self.cwd = [os.path.abspath(start_path)]
        self.out = None
        self.ret_code = None

    def run(self, cmd, expected_return_code=0):
        """Run command with args, return stdout merged with stderr."""
        args_list = shlex.split(cmd)
        proc = subprocess.Popen(args_list,
                                cwd=self.get_cwd(),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        self.out, err = proc.communicate()
        self.ret_code = proc.returncode

        if expected_return_code is not None:
            if expected_return_code != self.ret_code:
                raise RuntimeError("RETURN CODE %s, EXPECTED %s\n%s" %
                                   (self.ret_code,
                                    expected_return_code,
                                    self.out))
        return self.out

    def full_name(self, fname):
        return os.path.join(self.cwd[-1], fname)

    def write(self, fname, text):
        with open(self.full_name(fname), 'wb') as f:
            f.write(text)

    def read(self, fname):
        with open(self.full_name(fname), 'rb') as f:
            return f.read()

    @contextlib.contextmanager
    def cd(self, arg):
        self.cwd.append(os.path.abspath(os.path.join(self.cwd[-1], arg)))
        yield
        self.cwd.pop()

    def get_cwd(self):
        return self.cwd[-1]

    def mkdir(self, arg):
        os.makedirs(os.path.join(self.cwd[-1], arg))

    def rmtree(self):
        folder = self.cwd[-1]
        if os.path.exists(folder):
            shutil.rmtree(folder)


if __name__ == '__main__':
    # Example of usage
    folder = os.path.dirname(os.path.abspath(sys.argv[0]))
    new_folder1 = os.path.join(folder, 'new_folder1')

    ftr = FunctionalTestRunner(new_folder1)
    assert ftr.get_cwd() == new_folder1

    ftr.mkdir('new_folder2')
    with ftr.cd('new_folder2'):
        new_folder2 = os.path.join(new_folder1, 'new_folder2')
        assert ftr.get_cwd() == new_folder2
        ftr.rmtree()

    assert ftr.get_cwd() == new_folder1
    cmd = 'ipconfig' if sys.platform == "win32" else 'ipconfig'
    print(ftr.run(cmd))

    print(ftr.full_name('new_folder1'))
