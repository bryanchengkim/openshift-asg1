#!/usr/bin/perl

use strict;

print "Content-Type: text/plain\n\n";

sub foobar {
	my @array =();
	foreach my $i (@_) {
		push(@array,$i);
	}
	foreach my $i (@array) {
		print "$i\n";
	}
}

my @array = ("hello", "world");
foobar(@array);