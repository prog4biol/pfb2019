#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;

#mens	small	heather seafoam
#womens	medium	Heather Purple
#womens	medium	berry
#mens 	medium 	heather coral silk

my $shirtFile= 'shirts.txt';
open SHIRTS , $shirtFile or die "Cant open shirt txt file\n";
my %shirts;
while (my $line = <SHIRTS>){
  chomp $line;
  my ($style, $size, $color) = split "\t", $line;
  $shirts{lc $style}{lc $size}{lc $color}++;
}

foreach my $st (keys %shirts){
  foreach my $sz (keys  %{$shirts{$st}}){
    foreach my $co (keys %{$shirts{$st}{$sz}}){
      my $count = $shirts{$st}{$sz}{$co};
      print join("\t",$st,$sz,$co,$count),"\n";
    }

  }
}
