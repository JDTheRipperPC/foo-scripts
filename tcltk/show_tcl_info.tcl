#!/usr/bin/env tclsh

# Display some information about tcl variables

puts "auto_path: $auto_path\n"
puts "env array size: [array size env]"
set count 0
set aux ""
foreach item [array get env] {
    if {[expr {$count % 2}] == 0} {
	set aux $item
	set count [expr {$count + 1}]
    } else {
	puts "$aux $item"
	set count [expr {$count + 1}]
    }
}
puts ""
puts "tcl_patchLevel: $tcl_patchLevel\n"
puts "tcl_library: $tcl_library\n"
puts "tcl_pkgPath: $tcl_pkgPath\n"
puts "platform array size: [array size tcl_platform]"
set count 0
foreach item [array get tcl_platform] {
    if {[expr {$count % 2}] == 0} {
	set aux $item
	set count [expr {$count + 1}]
    } else {
	puts "$aux $item"
	set count [expr {$count + 1}]
    }
}
puts ""
puts "tcl_precision: $tcl_precision\n"
puts "tcl_rcFileName: $tcl_rcFileName\n"
puts "tcl_version: $tcl_version"
