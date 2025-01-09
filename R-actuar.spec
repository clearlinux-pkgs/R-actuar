#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-actuar
Version  : 3.3.5
Release  : 74
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/actuar_3.3-5.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/actuar_3.3-5.tar.gz
Summary  : Actuarial Functions and Heavy Tailed Distributions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-actuar-lib = %{version}-%{release}
Requires: R-expint
BuildRequires : R-expint
BuildRequires : buildreq-R

%description
modeling of loss distributions; risk theory and ruin theory;
  simulation of compound models, discrete mixtures and compound
  hierarchical models; credibility theory. Support for many additional
  probability distributions to model insurance loss size and

%package dev
Summary: dev components for the R-actuar package.
Group: Development
Requires: R-actuar-lib = %{version}-%{release}
Provides: R-actuar-devel = %{version}-%{release}
Requires: R-actuar = %{version}-%{release}

%description dev
dev components for the R-actuar package.


%package lib
Summary: lib components for the R-actuar package.
Group: Libraries

%description lib
lib components for the R-actuar package.


%prep
%setup -q -n actuar
pushd ..
cp -a actuar buildavx2
popd
pushd ..
cp -a actuar buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736456199

%install
export SOURCE_DATE_EPOCH=1736456199
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/actuar/CITATION
/usr/lib64/R/library/actuar/DESCRIPTION
/usr/lib64/R/library/actuar/INDEX
/usr/lib64/R/library/actuar/Meta/Rd.rds
/usr/lib64/R/library/actuar/Meta/data.rds
/usr/lib64/R/library/actuar/Meta/demo.rds
/usr/lib64/R/library/actuar/Meta/features.rds
/usr/lib64/R/library/actuar/Meta/hsearch.rds
/usr/lib64/R/library/actuar/Meta/links.rds
/usr/lib64/R/library/actuar/Meta/nsInfo.rds
/usr/lib64/R/library/actuar/Meta/package.rds
/usr/lib64/R/library/actuar/Meta/vignette.rds
/usr/lib64/R/library/actuar/NAMESPACE
/usr/lib64/R/library/actuar/NEWS.0.Rd
/usr/lib64/R/library/actuar/NEWS.1.Rd
/usr/lib64/R/library/actuar/NEWS.2.Rd
/usr/lib64/R/library/actuar/NEWS.Rd
/usr/lib64/R/library/actuar/R/actuar
/usr/lib64/R/library/actuar/R/actuar.rdb
/usr/lib64/R/library/actuar/R/actuar.rdx
/usr/lib64/R/library/actuar/data/Rdata.rdb
/usr/lib64/R/library/actuar/data/Rdata.rds
/usr/lib64/R/library/actuar/data/Rdata.rdx
/usr/lib64/R/library/actuar/demo/credibility.R
/usr/lib64/R/library/actuar/demo/lossdist.R
/usr/lib64/R/library/actuar/demo/risk.R
/usr/lib64/R/library/actuar/demo/simulation.R
/usr/lib64/R/library/actuar/doc/actuar.R
/usr/lib64/R/library/actuar/doc/actuar.Rnw
/usr/lib64/R/library/actuar/doc/actuar.pdf
/usr/lib64/R/library/actuar/doc/coverage.R
/usr/lib64/R/library/actuar/doc/coverage.Rnw
/usr/lib64/R/library/actuar/doc/coverage.pdf
/usr/lib64/R/library/actuar/doc/credibility.R
/usr/lib64/R/library/actuar/doc/credibility.Rnw
/usr/lib64/R/library/actuar/doc/credibility.pdf
/usr/lib64/R/library/actuar/doc/distributions.Rnw
/usr/lib64/R/library/actuar/doc/distributions.pdf
/usr/lib64/R/library/actuar/doc/index.html
/usr/lib64/R/library/actuar/doc/modeling.R
/usr/lib64/R/library/actuar/doc/modeling.Rnw
/usr/lib64/R/library/actuar/doc/modeling.pdf
/usr/lib64/R/library/actuar/doc/risk.R
/usr/lib64/R/library/actuar/doc/risk.Rnw
/usr/lib64/R/library/actuar/doc/risk.pdf
/usr/lib64/R/library/actuar/doc/simulation.R
/usr/lib64/R/library/actuar/doc/simulation.Rnw
/usr/lib64/R/library/actuar/doc/simulation.pdf
/usr/lib64/R/library/actuar/help/AnIndex
/usr/lib64/R/library/actuar/help/actuar.rdb
/usr/lib64/R/library/actuar/help/actuar.rdx
/usr/lib64/R/library/actuar/help/aliases.rds
/usr/lib64/R/library/actuar/help/paths.rds
/usr/lib64/R/library/actuar/html/00Index.html
/usr/lib64/R/library/actuar/html/R.css
/usr/lib64/R/library/actuar/po/en@quot/LC_MESSAGES/R-actuar.mo
/usr/lib64/R/library/actuar/po/en@quot/LC_MESSAGES/actuar.mo
/usr/lib64/R/library/actuar/po/fr/LC_MESSAGES/R-actuar.mo
/usr/lib64/R/library/actuar/po/fr/LC_MESSAGES/actuar.mo
/usr/lib64/R/library/actuar/po/it/LC_MESSAGES/R-actuar.mo
/usr/lib64/R/library/actuar/po/it/LC_MESSAGES/actuar.mo
/usr/lib64/R/library/actuar/tests/betaint-tests.R
/usr/lib64/R/library/actuar/tests/dpqr-tests.R
/usr/lib64/R/library/actuar/tests/rcompound-tests.R
/usr/lib64/R/library/actuar/tests/rmixture-tests.R

%files dev
%defattr(-,root,root,-)
/usr/lib64/R/library/actuar/include/actuarAPI.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/actuar/libs/actuar.so
/V4/usr/lib64/R/library/actuar/libs/actuar.so
/usr/lib64/R/library/actuar/libs/actuar.so
