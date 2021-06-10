"""Tests for transform.py"""
import os

import bencode


def test_transform_bencode_data_1():
    """Try to transform some bencoded data"""
    source_data = " \t \r \n \\ \" /'`[]".encode("ascii")
    data_as_string = bencode.be_to_str(source_data)
    assert data_as_string == " [09] [0d] [0a] [5c] [22] [2f][27][60][5b][5d]"


def test_transform_bencode_data_2(datadir):
    """Try to transform some bencoded data"""
    torrent_data = datadir["big-buck-bunny.torrent"].read("rb")
    torrent_data_dec = bencode.decode(torrent_data)
    torrent_data_dec[b"info"].pop(b"pieces")
    data_as_string = bencode.be_to_str(bencode.encode(torrent_data_dec))
    assert data_as_string == (
        "d8:announce40:udp:[2f][2f]tracker.leechers-paradise.org:696913:"
        "announce-listll40:udp:[2f][2f]tracker.leechers-paradise.org:"
        "6969el34:udp:[2f][2f]tracker.coppersurfer.tk:6969el33:udp:[2f][2f]"
        "tracker.opentrackr.org:1337el23:udp:[2f][2f]explodie.org:6969el31:"
        "udp:[2f][2f]tracker.empire-js.us:1337el26:wss:[2f][2f]tracker."
        "btorrent.xyzel32:wss:[2f][2f]tracker.openwebtorrent.comel25:wss:"
        "[2f][2f]tracker.fastcast.nzee7:comment34:WebTorrent <https:[2f][2f]"
        "webtorrent.io>10:created by34:WebTorrent <https:[2f][2f]webtorrent."
        "io>13:creation datei1490916601e8:encoding5:UTF-84:infod5:filesld6:"
        "lengthi140e4:pathl21:Big Buck Bunny.en.srteed6:lengthi276134947e4:"
        "pathl18:Big Buck Bunny.mp4eed6:lengthi310380e4:pathl10:poster."
        "jpgeee4:name14:Big Buck Bunny12:piece lengthi262144ee8:url-listl31:"
        "https:[2f][2f]webtorrent.io[2f]torrents[2f]ee"
    )


def test_transform_torrent_file(datadir):
    """Try to transform a torrent file"""
    torrent_data = datadir["big-buck-bunny.torrent"].read("rb")
    data_as_string = bencode.be_to_str(torrent_data)
    data_as_bytes = bencode.str_to_be(data_as_string)
    assert torrent_data == data_as_bytes


def test_transform_random_data():
    """Try to transform a random sequence of bytes"""
    source_data = os.urandom(10 ** 5)
    data_as_string = bencode.be_to_str(source_data)
    data_as_bytes = bencode.str_to_be(data_as_string)
    assert source_data == data_as_bytes
