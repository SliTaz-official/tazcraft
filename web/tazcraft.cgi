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

# Get a value in
get_value() {
	val=$(grep ^${1}= ${config} | cut -d "=" -f 2)
	cat << EOT
<tr>
	<td>$1</td>
	<td>$val</td>
</tr>
EOT
}

# HTML header
cat << EOT
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>Tazcraft</title>
	<link rel="stylesheet" href="http://play.slitaz.me/style.css" />
</head>
<body>
<header>
	<div id="logo"></div>
	<div id="network">
		<a href="http://play.slitaz.me">play.SliTaz.me</a>
		<a href="http://www.slitaz.org">SliTaz.org</a>
	</div>
	<h1>Tazcraft Server</h1>
</header>
<div id="content">

<h2>Welcome to Tazcraft</h2>
<p>A SliTaz GNU/Linux Minecraft server</p>
<pre>
<img src="minecraft.png" alt="*" />Server address: <b>play.slitaz.me</b>
</pre>

<h3>Configuration</h3>
<table>
	<thead>
		<td>$(gettext "Variable")</td>
		<td>$(gettext "Value")</td>
	</thead>
EOT

for var in gamemode server-port level-name difficulty max-players; do
	get_value ${var}
done

# HTML footer
cat << EOT
</table>
</div>
<footer></footer>
</body>
</htnl>
EOT
exit 0
