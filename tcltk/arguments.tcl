#!/usr/bin/env tclsh

puts "Argument count: $argc"
foreach arg $argv {
    puts "Argument: $arg"
}
puts "Start script: $argv0"

if {$::argv0 eq [info script]} {
    puts "This can be used as the python equivalent: if __main__ == '__main__'"
}
