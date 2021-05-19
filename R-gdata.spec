#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gdata
Version  : 2.18.0
Release  : 36
URL      : https://cran.r-project.org/src/contrib/gdata_2.18.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gdata_2.18.0.tar.gz
Summary  : Various R Programming Tools for Data Manipulation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gtools
BuildRequires : R-gtools
BuildRequires : buildreq-R

%description
- medical unit conversions ('ConvertMedUnits', 'MedUnits'),
   - combining objects ('bindData', 'cbindX', 'combine', 'interleave'),
   - character vector operations ('centerText', 'startsWith', 'trim'),
   - factor manipulation ('levels', 'reorder.factor', 'mapLevels'),
   - obtaining information about R objects ('object.size', 'elem', 'env',
     'humanReadable', 'is.what', 'll', 'keep', 'ls.funs',
     'Args','nPairs', 'nobs'),
   - manipulating MS-Excel formatted files ('read.xls',
     'installXLSXsupport', 'sheetCount', 'xlsFormats'),
   - generating fixed-width format files ('write.fwf'),
   - extricating components of date & time objects ('getYear', 'getMonth',
     'getDay', 'getHour', 'getMin', 'getSec'),
   - operations on columns of data frames  ('matchcols', 'rename.vars'),
   - matrix operations ('unmatrix', 'upperTriangle', 'lowerTriangle'),
   - operations on vectors ('case', 'unknownToNA', 'duplicated2', 'trimSum'),
   - operations on data frames ('frameApply', 'wideByFactor'),
   - value of last evaluated expression ('ans'), and
   - wrapper for 'sample' that ensures consistent behavior for both
     scalar and vector arguments ('resample').

%prep
%setup -q -c -n gdata
cd %{_builddir}/gdata

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616003350

%install
export SOURCE_DATE_EPOCH=1616003350
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdata
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdata
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gdata || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gdata/ChangeLog
/usr/lib64/R/library/gdata/DESCRIPTION
/usr/lib64/R/library/gdata/INDEX
/usr/lib64/R/library/gdata/Meta/Rd.rds
/usr/lib64/R/library/gdata/Meta/data.rds
/usr/lib64/R/library/gdata/Meta/features.rds
/usr/lib64/R/library/gdata/Meta/hsearch.rds
/usr/lib64/R/library/gdata/Meta/links.rds
/usr/lib64/R/library/gdata/Meta/nsInfo.rds
/usr/lib64/R/library/gdata/Meta/package.rds
/usr/lib64/R/library/gdata/Meta/vignette.rds
/usr/lib64/R/library/gdata/NAMESPACE
/usr/lib64/R/library/gdata/NEWS
/usr/lib64/R/library/gdata/R/gdata
/usr/lib64/R/library/gdata/R/gdata.rdb
/usr/lib64/R/library/gdata/R/gdata.rdx
/usr/lib64/R/library/gdata/bin/xls2csv
/usr/lib64/R/library/gdata/bin/xls2csv.bat
/usr/lib64/R/library/gdata/data/MedUnits.rda
/usr/lib64/R/library/gdata/doc/gregmisc.pdf
/usr/lib64/R/library/gdata/doc/index.html
/usr/lib64/R/library/gdata/doc/mapLevels.R
/usr/lib64/R/library/gdata/doc/mapLevels.Rnw
/usr/lib64/R/library/gdata/doc/mapLevels.pdf
/usr/lib64/R/library/gdata/doc/unknown.R
/usr/lib64/R/library/gdata/doc/unknown.Rnw
/usr/lib64/R/library/gdata/doc/unknown.pdf
/usr/lib64/R/library/gdata/help/AnIndex
/usr/lib64/R/library/gdata/help/aliases.rds
/usr/lib64/R/library/gdata/help/gdata.rdb
/usr/lib64/R/library/gdata/help/gdata.rdx
/usr/lib64/R/library/gdata/help/paths.rds
/usr/lib64/R/library/gdata/html/00Index.html
/usr/lib64/R/library/gdata/html/R.css
/usr/lib64/R/library/gdata/perl/Archive/README-Archive-Zip
/usr/lib64/R/library/gdata/perl/Archive/Zip.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/Archive.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/BufferedFileHandle.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/DirectoryMember.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/FAQ.pod
/usr/lib64/R/library/gdata/perl/Archive/Zip/FileMember.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/Member.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/MemberRead.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/MockFileHandle.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/NewFileMember.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/StringMember.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/Tree.pm
/usr/lib64/R/library/gdata/perl/Archive/Zip/ZipFileMember.pm
/usr/lib64/R/library/gdata/perl/Crypt/RC4.pm
/usr/lib64/R/library/gdata/perl/Digest/Perl/MD5.pm
/usr/lib64/R/library/gdata/perl/Graphics/ColorUtils.pm
/usr/lib64/R/library/gdata/perl/IO/AtomicFile.pm
/usr/lib64/R/library/gdata/perl/IO/InnerFile.pm
/usr/lib64/R/library/gdata/perl/IO/Lines.pm
/usr/lib64/R/library/gdata/perl/IO/Scalar.pm
/usr/lib64/R/library/gdata/perl/IO/Scalar.pm.html
/usr/lib64/R/library/gdata/perl/IO/ScalarArray.pm
/usr/lib64/R/library/gdata/perl/IO/Stringy.pm
/usr/lib64/R/library/gdata/perl/IO/Wrap.pm
/usr/lib64/R/library/gdata/perl/IO/WrapTie.pm
/usr/lib64/R/library/gdata/perl/OLE/README-OLE-Storage_Lite
/usr/lib64/R/library/gdata/perl/OLE/Storage_Lite.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Cell.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Dump.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/FmtDefault.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/FmtJapan.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/FmtJapan2.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/FmtUnicode.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Font.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Format.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/SaveParser.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/SaveParser/Workbook.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/SaveParser/Worksheet.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Utility.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Workbook.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseExcel/Worksheet.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/ParseXLSX.pm
/usr/lib64/R/library/gdata/perl/Spreadsheet/README-ParseExcel
/usr/lib64/R/library/gdata/perl/Spreadsheet/README-XLS
/usr/lib64/R/library/gdata/perl/VERSIONS
/usr/lib64/R/library/gdata/perl/XML/Twig.pm
/usr/lib64/R/library/gdata/perl/XML/Twig/XPath.pm
/usr/lib64/R/library/gdata/perl/install_modules.pl
/usr/lib64/R/library/gdata/perl/module_tools.pl
/usr/lib64/R/library/gdata/perl/sheetCount.pl
/usr/lib64/R/library/gdata/perl/sheetNames.pl
/usr/lib64/R/library/gdata/perl/supportedFormats.pl
/usr/lib64/R/library/gdata/perl/xls2csv.pl
/usr/lib64/R/library/gdata/perl/xls2tab.pl
/usr/lib64/R/library/gdata/perl/xls2tsv.pl
/usr/lib64/R/library/gdata/tests/runRUnitTests.R
/usr/lib64/R/library/gdata/tests/test.humanReadable.R
/usr/lib64/R/library/gdata/tests/test.humanReadable.Rout.save
/usr/lib64/R/library/gdata/tests/test.read.xls.R
/usr/lib64/R/library/gdata/tests/test.read.xls.Rout.save
/usr/lib64/R/library/gdata/tests/test.reorder.factor.R
/usr/lib64/R/library/gdata/tests/test.reorder.factor.Rout.save
/usr/lib64/R/library/gdata/tests/test.write.fwf.eol.R
/usr/lib64/R/library/gdata/tests/tests.write.fwf.R
/usr/lib64/R/library/gdata/tests/tests.write.fwf.Rout.save
/usr/lib64/R/library/gdata/tests/unitTests/Makefile
/usr/lib64/R/library/gdata/tests/unitTests/runit.bindData.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.cbindX.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.drop.levels.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.getDateTimeParts.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.mapLevels.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.nPairs.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.reorder.factor.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.trim.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.trimSum.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.unknown.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.wideByFactor.R
/usr/lib64/R/library/gdata/tests/unitTests/runit.write.fwf.R
/usr/lib64/R/library/gdata/xls/ExampleExcelFile.xls
/usr/lib64/R/library/gdata/xls/ExampleExcelFile.xlsx
/usr/lib64/R/library/gdata/xls/ExampleExcelFile_1900.xls
/usr/lib64/R/library/gdata/xls/ExampleExcelFile_1900.xlsx
/usr/lib64/R/library/gdata/xls/ExampleExcelFile_1904.xls
/usr/lib64/R/library/gdata/xls/ExampleExcelFile_1904.xlsx
/usr/lib64/R/library/gdata/xls/iris.xls
/usr/lib64/R/library/gdata/xls/latin-1.xls
/usr/lib64/R/library/gdata/xls/latin-1.xlsx
/usr/lib64/R/library/gdata/xls/wide.xls
/usr/lib64/R/library/gdata/xls/wide.xlsx
