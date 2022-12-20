Name: freecell-solver
Version: 5.0.0
Release: 1
License: MIT
Group: Amusement/Games
Source: http://fc-solve.shlomifish.org/downloads/fc-solve/freecell-solver-%{version}.tar.xz
URL: http://fc-solve.shlomifish.org/
Requires: libfreecell-solver0 = %{version}
Summary: The Freecell Solver Executable
BuildRequires: cmake
BuildRequires: gmp-devel
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Env::Path)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which)
BuildRequires: perl(Games::Solitaire::Verify)
BuildRequires: perl(Games::Solitaire::Verify::Solution)
BuildRequires: perl(Inline)
BuildRequires: perl(Inline::C)
BuildRequires: perl(IPC::Open2)
BuildRequires: perl(lib)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moo)
BuildRequires: perl(MooX)
BuildRequires: perl(MooX::late)
BuildRequires: perl(parent)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(String::ShellQuote)
BuildRequires: perl(Template)
BuildRequires: perl(Test::Data::Split)
BuildRequires: perl(Test::Data::Split::Backend::Hash)
BuildRequires: perl(Test::Data::Split::Backend::ValidateHash)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::PerlTidy)
BuildRequires: perl(Test::RunValgrind)
BuildRequires: perl(Test::TrailingSpace)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(warnings)
BuildRequires: perl(YAML::XS)
BuildRequires: perl-devel >= 5.14.0
BuildRequires: python3-random2
BuildRequires: tap-devel
BuildRequires: the_silver_searcher
BuildRequires: valgrind

%description
The Freecell Solver package contains the fc-solve executable which is
a command-line program that can be used to solve games of Freecell and
similar card solitaire variants.

This package also contains command line executables to generate the initial
boards of several popular Freecell implementations.

%package -n libfreecell-solver0
Summary: The Freecell Solver dynamic libraries for solving Freecell games
Group: Amusement/Games

%description -n libfreecell-solver0
Contains the Freecell Solver libraries that are used by some programs to solve
games of Freecell and similar variants of card solitaire.

This package is mandatory for the Freecell Solver executable too.

%package -n libfreecell-solver-devel
Summary: The Freecell Solver development tools for solving Freecell games
Group: Amusement/Games
Requires: libfreecell-solver0 = %{version}

%description -n libfreecell-solver-devel
Freecell Solver is a library for automatically solving boards of Freecell and
similar variants of card Solitaire. This package contains the header files and
static libraries necessary for developing programs using Freecell Solver.

You should install it if you are a game developer who would like to use
Freecell Solver from within your programs.

%package -n libfreecell-solver0-static
Summary: The Freecell Solver static libraries
Group: Amusement/Games
Requires: libfreecell-solver0 = %{version}

%description -n libfreecell-solver0-static
Freecell Solver is a library for automatically solving boards of Freecell and
similar variants of card Solitaire. This package contains the static libraries.

It is not generally required.

%prep
%setup

%build
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DMAX_NUM_FREECELLS=8 -DMAX_NUM_STACKS=12
%make_build

%check
cd build
perl ../run-tests.pl

%install
cd build
%make_install

%files -n libfreecell-solver0
%{_libdir}/libfreecell-solver.so.*
/usr/share/freecell-solver/presetrc
/usr/share/freecell-solver/presets/*

%files -n libfreecell-solver0-static
%{_libdir}/libfreecell-solver.a

%files
%defattr(-,root,root)
/usr/bin/fc-solve
/usr/bin/fc_solve_find_index_s2ints.py
/usr/bin/find-freecell-deal-index.py
/usr/bin/freecell-solver-fc-pro-range-solve
/usr/bin/freecell-solver-multi-thread-solve
/usr/bin/freecell-solver-range-parallel-solve
/usr/bin/gen-multiple-pysol-layouts
/usr/bin/make_pysol_freecell_board.py
/usr/bin/pi-make-microsoft-freecell-board
/usr/bin/transpose-freecell-board.py
%{_mandir}/*/*
%{_docdir}/*

%files -n libfreecell-solver-devel
%defattr(-,root,root)
/usr/include/freecell-solver/*.h
%{_libdir}/libfreecell-solver.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 31 2009 Shlomi Fish <shlomif@iglu.org.il> 2.21.2-1
- Adapted to the CMake build system.
- Changed the license from "Public Domain" to "MIT".

* Mon Oct 24 2005 Shlomi Fish <shlomif@iglu.org.il> 2.8.11-1
- Changed "Copyright" to "License"

* Fri Jul 30 2004 Shlomi Fish <shlomif@iglu.org.il> 2.8.7-1
- Added some unpackaged files
- deleted make-microsoft-freecell-board so it won't be reported as
  unpacked
- removed some old cd's that are now useless
- removed the serial tags - they are just trouble.

* Mon Sep 02 2002 Shlomi Fish <shlomif@iglu.org.il> 2.7.15-1
- Used strip on the range solver
- Added the presets' related files

* Sat Feb 16 2002 Shlomi Fish <shlomif@iglu.org.il> 2.1.10-1
- updated to version 2.1.10
- removed the man pages symlinks (they were superceded by the ".so" links).

* Fri Jan 04 2002 Shlomi Fish <shlomif@iglu.org.il> 2.0.1-1
- updated to version 2.0.1
- added freecell-solver-range-parallel-solve to the /usr/bin programs

* Tue Dec 18 2001 Shlomi Fish <shlomif@iglu.org.il> 2.0.0-1
- updated to version 2.0.0

* Fri Nov 23 2001 Shlomi Fish <shlomif@iglu.org.il> 1.10.3-1
- updated to version 1.10.3

* Thu Nov 22 2001 Shlomi Fish <shlomif@iglu.org.il> 1.10.2-1
- updated to version 1.10.2

* Tue Oct 02 2001 Shlomi Fish <shlomif@iglu.org.il> 1.10.0-1
- updated to version 1.10.0

* Sat Sep 22 2001 Shlomi Fish <shlomif@iglu.org.il> 1.8.2-1
- updated to version 1.8.2

* Sat Sep 01 2001 Shlomi Fish <shlomif@iglu.org.il> 1.8.0-1
- Changed the version to 1.8.0
- Removed the -autconf suffix from the archive.

* Sat Jul 07 2001 Shlomi Fish <shlomif@iglu.org.il> 1.6.7-2
- Fixed the man pages.
- Included a paragraph about the board_gen programs in the description of
  the executable package.

* Sat Jun 09 2001 Shlomi Fish <shlomif@iglu.org.il> 1.6.7-1
- Changed the version to 1.6.7.
- Added support for the man pages.
- Added the symlinked man pages.
- Added the board_gen sub-dir in the documentation directory. (using a rather
crude hack)
- Known Bugs:
    1 - The man pages need a little rework, there are some typos and they
        don't look very standard.


* Thu May 24 2001 Shlomi Fish <shlomif@iglu.org.il> 1.6.4-3
- Added the board generation programs into the RPM.
- Changed the package to my name and E-mail. Done through the home-dir conf
file, not by editting the SPEC, but what the heck.

* Sat May 19 2001 Shlomi Fish <shlomif@iglu.org.il> 1.6.4-2
- Changed the descriptions and summaries to something more meaningful
- Removed the dependency on "Serial" in "Requires".

* Fri May 18 2001 Shlomi Fish <shlomif@iglu.org.il> 1.6.4-1
- First working version with libs and executable support.
- Known Bugs:
      1 - No "devel" package.
      2 - No options passed to "configure".
- Added calls to strip.
- "configure" is now OK with all the options set.
- Added Headers and a working freecell-solver-devel
