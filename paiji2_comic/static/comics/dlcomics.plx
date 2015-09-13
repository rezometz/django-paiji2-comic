#!/usr/bin/env perl
# dlcomics.plx
# should be run by a daily cron
use strict;
use warnings;
use WWW::Mechanize;
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
	print "trying getting $comic\n";
	my $date = DateTime->now();
	my $filename = "$comic--$date";
	my $link = "$comic";
	my $url = "$baseurl$comic";

	$mech->get($url);

	my $strip = $mech->find_image(
		url_regex => qr/assets\.amuniversal\.com/,
	);

	print $strip->url(), "\n";

	$mech->get($strip->url());

	if (open(my $file, '<', $link))
	{
		binmode($file);
		if (md5_hex($mech->content()) eq Digest::MD5->new()->addfile($file)->hexdigest())
		{
			print "same file\n";
			next;
		}
	}
	{
		$mech->save_content(
			"$filename",
			binmode => ':raw',
		);
		link("$filename", "$link");
	}
}
