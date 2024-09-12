Name:           vaultx
Version:        1.0.0
Release:        1%{?dist}
Summary:        Comprehensive Vault Cluster Status Checker

License:        MIT
URL:            https://github.com/zbaban/vaultx
Source0:        %{name}-%{version}.tar.gz

Requires:       bash vault jq

%description
vaultx provides a comprehensive status check for Vault clusters,
including node discovery, status checks, and various Vault operations.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 vaultx $RPM_BUILD_ROOT/%{_bindir}/vaultx

%files
%{_bindir}/vaultx

%changelog
* Thu Sep 12 2024 Zaid Baban <zaidbaban@gmail> - 1.0.0-1
- Initial package release
