#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.63])
AC_INIT([fcgiwrap], [1.1.0], [root@localdomain.pl])
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([fcgiwrap.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.
AC_CHECK_LIB([fcgi], [FCGX_Init],, [AC_MSG_ERROR([FastCGI library is missing])])

# Checks for header files.
AC_CHECK_HEADERS([arpa/inet.h fcntl.h limits.h netinet/in.h stdlib.h string.h sys/socket.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_TYPE_SSIZE_T

# Checks for library functions.
AC_FUNC_FORK
AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK
AC_FUNC_MALLOC
AC_CHECK_FUNCS([dup2 putenv select setenv socket strchr strdup strerror strrchr])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
