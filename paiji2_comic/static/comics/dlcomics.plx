#!/usr/bin/env perl
# dlcomics.plx
# should be run by a daily cron
use strict;
use warnings;
use WWW::Mechanize;
use DateTime;
# use Data::Dumper qw(Dumper);
use Digest::MD5 qw(md5_hex);

# settings
my $mech = WWW::Mechanize->new(
	autocheck => 1,
);

$mech->agent_alias('Windows Mozilla');

my @slugs = qw(
	calvinandhobbes
	nancy
	that-is-priceless
);

my $baseurl = 'http://www.gocomics.com/';


# fetching
for my $slug (@slugs)
{
	my $date = DateTime->now();
	print "\n$date : trying getting $slug\n";
	my $filename = $slug;
	my $url = "$baseurl$slug";

	$mech->get($url);

	my $strip = (
		$mech->find_all_images(url_regex => qr/assets\.amuniversal\.com/)
	)[1];  # second img (better quality)

	$mech->get($strip->url());
	print "downloaded ", $strip->url(), "\n";

	if (open(my $fh, '<', $filename))
	{
		print "opening $filename", "\n";
		binmode($fh);
		if (md5_hex($mech->content()) eq Digest::MD5->new()->addfile($fh)->hexdigest())
		{
			print "same file\n";
			close($fh);
			print "closing $filename", "\n";
			next;
		}
		close($fh);
		print "closing $filename", "\n";
	}
	$mech->save_content(
		"$filename",
		binmode => ':raw',
	);
	print "saving as $filename", "\n";
}
exit 0;
