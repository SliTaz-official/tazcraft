#!/bin/sh
#
# tazcraft.cgi - A Minecraft server info/admin CGI interface
#
# Authors: Kayam Lincoln-Vazquez, Christophe Lincoln
# Copyright (C) 2017 SliTaz GNU/Linux - BSD License
#
. /usr/lib/slitaz/httphelper.sh
header

home="/home/minecraft"
server="$home/server"
config="$server/server.properties"
whitelist="${server}/whitelist.json"

# Get a key value from server config file
get_key() {
	val=$(grep ^${1}= ${config} | cut -d "=" -f 2)
	cat << EOT
<tr>
	<td>$1</td>
	<td>$val</td>
</tr>
EOT
}

# HTML footer
html_footer() {
	cat << EOT
</div>
<footer style="text-align: center; margin: 10px; color: #888;">
	&copy; $(date '+%Y') <a href="http://www.slitaz.org">SliTaz GNU/Linux</a>
</footer>
</body>
</htnl>
EOT
}

# HTML header
html_header() {
	cat << EOT
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>Tazcraft - $1</title>
	<link rel="stylesheet" href="http://play.slitaz.me/style.css" />
</head>
<body>
<header>
	<div id="logo"></div>
	<div id="network">
		<a href="tazcraft.cgi">Tazcraft</a>
		<a href="tazcraft.cgi?README">README</a>
		<span style="color: #682368;">&hearts;</span> 
		<a href="http://play.slitaz.me">play.SliTaz.me</a>
	</div>
	<h1>Tazcraft Server</h1>
</header>
<div id="content">
EOT
}

#
# Handle GET commands
#

case " $(GET) " in
	
	*\ README\ *)
		
		if [ -f "../README" ]; then
			README="../README"
		else
			README="/usr/share/doc/slitaz/tazcraft.txt"
		fi
		
		html_header "README"
		echo "<h2>README</h2>"
		echo "<pre>"
		# Let have a few color in README
		cat ${README} | sed \
			-e "/^====.*/"d -e "/^----.*/"d \
			-e s"#==\([^']*\)==#<h3 style='margin: 0;'>\1</h3>#"g \
			-e s"#^	[\#|\$|\/]\([^']*\)#<span style='color: green;'>\0</span>#"g \
			-e s"#http://\([^']*\).*#<a href='\0'>\0</a>#"g
		echo "</pre>"
		html_footer 
		exit 0 ;;
	
esac

#
# Home page with server information and configuration
#
html_header "Welcome"

uptime=$(ps | grep minecraft_server | grep -v grep | awk '{print $3}')
if [ ! "$uptime" ]; then
	uptime="Not running"
fi

cat << EOT
<h2>Welcome to Tazcraft</h2>
<p>
	A SliTaz GNU/Linux Minecraft server
	- Uptime: <span style="color: green;">$uptime</span>
</p>

<pre>
<img src="minecraft.png" alt="*" />Server address: \
<span style="color: green; font-size: 20px;">play.slitaz.me</span>
</pre>

<h3>Configuration</h3>
<table>
	<thead>
		<td>$(gettext "Key")</td>
		<td>$(gettext "Value")</td>
	</thead>
EOT

for var in gamemode server-port level-name difficulty max-players \
	allow-flight white-list
do
	get_key ${var}
done
echo "</table>"

# White listed users names
if grep -q "white-list=true" ${config}; then
	echo "<h3>White list</h3>"
	echo "<pre>"
	fgrep name ${whitelist} | cut -d '"' -f 4
	echo "</pre>"
fi

html_footer
exit 0
