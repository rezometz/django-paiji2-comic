#!/usr/bin/env perl
# dlcomics.plx
# should be run by a daily cron
use strict;
use warnings;
use WWW::Mechanize;
# use Data::Dumper qw(Dumper);
use Digest::MD5 qw(md5_hex);
use DateTime;


# settings
#
my $mech = WWW::Mechanize->new(
	noproxy => 1,
	autocheck => 1,
);

$mech->agent_alias('Windows Mozilla');

my @comics = qw(
	calvinandhobbes
	nancy
);

my $baseurl = 'http://www.gocomics.com/';


# fetching
#
for my $comic (@comics)
{
	my $date = DateTime->now();
	print "\n$date : trying getting $comic\n";
	my $filename = "$comic--$date";
	my $link = "$comic";
	my $url = "$baseurl$comic";

	$mech->get($url);

	my @strips = $mech->find_all_images(
		url_regex => qr/assets\.amuniversal\.com/,
	);

	my $strip = $strips[1];  # second img (better quality)

	$mech->get($strip->url());
	print "downloaded ", $strip->url(), "\n";

	if (open(my $file, '<', $link))
	{
		print "opening $file", "\n";
		binmode($file);
		if (md5_hex($mech->content()) eq Digest::MD5->new()->addfile($file)->hexdigest())
		{
			print "same file\n";
			close($file);
			next;
		}
		close($file);
	}
	$mech->save_content(
		"$filename",
		binmode => ':raw',
	);
	print "saving as $filename", "\n";
	link("$filename", "$link");
	print "linking as $link", "\n";

}
exit 0;
