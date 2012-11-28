Name:           squashfs
Version:        4.2
Release:        0
License:        GPL-2.0+
Summary:        A Read-Only File System with Efficient Compression
Url:            http://squashfs.sourceforge.net/
Group:          System/Filesystems
Source0:        %{name}%{version}.tar.gz
BuildRequires:  attr-devel
BuildRequires:  lzma-devel
BuildRequires:  lzo-devel
BuildRequires:  zlib-devel
Supplements:    filesystem(squashfs)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the userland utilities to create and read
squashfs images.

%prep
%setup -n squashfs%{version}

%build
sed -i -e "s#-O2#%{optflags}#g" squashfs-tools/Makefile
make %{?_smp_mflags} -C squashfs-tools XZ_SUPPORT=1 LZO_SUPPORT=1

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 squashfs-tools/{un,mk}squashfs %{buildroot}/usr/bin

%files
%defattr(-,root,root)
%license COPYING
/usr/bin/*squashfs

%changelog
