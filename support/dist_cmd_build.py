"""
An extension distutils' build to handle Python/Cython build of PyBayes
"""

from distutils.command.build import build as orig_build


class build(orig_build):
    """Introduce additional build step to inject Cython extensions"""

    def finalize_options(self):
        orig_build.finalize_options(self)
        # prepend our custom command
        self.sub_commands = [('build_prepare', None)] + self.sub_commands
        self.build_lib = self.build_platlib
        if self.distribution.profile:
            # so that profiling and non-profiling builds do not clash
            self.build_lib += '-profile'
            # Cython would otherwise think that .c files need not be regenerated:
            self.build_temp += '-profile'
