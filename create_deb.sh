#!/bin/bash


date=$(date +'%Y-%m-%d')
date_version=$(date +'%Y.%m.%d')
package_name="vdrrecinfo"

unterstrich="_"
tmp_dir=/tmp/$package_name$unterstrich$unterstrich$date
deb_name=$package_name$unterstrich$date_version
deb_dir=$tmp_dir/$deb_name

rm -R $tmp_dir

#mkdir -p $deb_dir
mkdir -p $deb_dir/DEBIAN

create_control() {
  echo $1 >> $deb_dir/DEBIAN/control
}

mkdir -p $deb_dir

create_control "Package: $package_name"
create_control "Version: $date_version"
create_control "Security: base"
create_control "Priority: optional"
create_control "Architecture: all"
create_control "Depends: python3"
#create_control "Maintainer: JG <cadivus@daverkomp.de>"
create_control "Description: Is for modifying strings in bash-scripts"

mkdir -p $deb_dir/usr/lib
cp -R -v src $deb_dir/usr/lib/$package_name
mkdir -p $deb_dir/usr/bin
ln -s /usr/lib/$package_name/vdrrecinfo_terminalui.py $deb_dir/usr/bin/$package_name

dpkg-deb --build $deb_dir
cp "$deb_dir.deb" "$deb_name.deb"
rm -R $tmp_dir
