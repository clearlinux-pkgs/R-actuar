#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-actuar
Version  : 2.3.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/actuar_2.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/actuar_2.3-1.tar.gz
Summary  : Actuarial Functions and Heavy Tailed Distributions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-actuar-lib = %{version}-%{release}
BuildRequires : R-expint
BuildRequires : buildreq-R

%description
modeling of loss distributions; risk theory and ruin theory;
  simulation of compound models, discrete mixtures and compound
  hierarchical models; credibility theory. Support for many additional
  probability distributions to model insurance loss amounts and loss

%package lib
Summary: lib components for the R-actuar package.
Group: Libraries

%description lib
lib components for the R-actuar package.


%prep
%setup -q -c -n actuar

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552944280

%install
export SOURCE_DATE_EPOCH=1552944280
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library actuar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library actuar
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library actuar
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  actuar || :


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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/actuar/libs/actuar.so
/usr/lib64/R/library/actuar/libs/actuar.so.avx2
/usr/lib64/R/library/actuar/libs/actuar.so.avx512
