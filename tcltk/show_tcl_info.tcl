#!/usr/bin/env tclsh

# Display some information about tcl variables

puts "auto_path: $auto_path\n"
puts "env array size: [array size env]"
foreach item [array get env] {
    puts "Env $item"
}
puts ""
puts "tcl_patchLevel: $tcl_patchLevel\n"
puts "tcl_library: $tcl_library\n"
puts "tcl_pkgPath: $tcl_pkgPath\n"
puts "platform array size: [array size tcl_platform]"
foreach item [array get tcl_platform] {
    puts "tcl_platform: $item"
}
puts ""
puts "tcl_precision: $tcl_precision\n"
puts "tcl_rcFileName: $tcl_rcFileName\n"
puts "tcl_version: $tcl_version"
