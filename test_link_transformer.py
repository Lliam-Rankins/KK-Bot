import pytest
from link_transformer import format_message, transform_urls


class TestDiscordUserLinkScenarios:
    """Tests verify expected behavior for realistic Discord message scenarios."""

    def test_single_instagram_reel_with_tracking_query(self):
        message = "Check this out https://www.instagram.com/reel/C7xyz123/?igsh=MWQ12345"
        expected = ["https://www.kkclip.com/reel/C7xyz123"]
        assert transform_urls(message) == expected

    def test_instagram_post_without_www(self):
        message = "look at this photo https://instagram.com/p/C9abc123/"
        expected = ["https://www.kkclip.com/p/C9abc123"]
        assert transform_urls(message) == expected

    def test_tiktok_standard_video_with_share_tokens(self):
        message = "best video https://www.tiktok.com/@creator/video/7123456789012345678?_t=8abcd&_r=1"
        expected = ["https://www.kkclip.com/@creator/video/7123456789012345678"]
        assert transform_urls(message) == expected

    def test_tiktok_mobile_shortlink(self):
        message = "sent from phone https://vm.tiktok.com/ZMxxxxxx/"
        expected = ["https://www.kkclip.com/ZMxxxxxx"]
        assert transform_urls(message) == expected

    def test_url_with_trailing_sentence_punctuation(self):
        message = "Did you see https://www.instagram.com/reel/C7xyz123/?"
        expected = ["https://www.kkclip.com/reel/C7xyz123"]
        assert transform_urls(message) == expected

    def test_url_inside_parentheses(self):
        message = "Here is the source (https://www.tiktok.com/@creator/video/7123456789012345678)."
        expected = ["https://www.kkclip.com/@creator/video/7123456789012345678"]
        assert transform_urls(message) == expected

    def test_message_with_both_instagram_and_tiktok(self):
        message = (
            "Instagram: https://www.instagram.com/reel/C7xyz123/?igsh=1 "
            "TikTok: https://www.tiktok.com/@user/video/9876543210"
        )
        expected = [
            "https://www.kkclip.com/reel/C7xyz123",
            "https://www.kkclip.com/@user/video/9876543210",
        ]
        assert transform_urls(message) == expected

    def test_duplicate_links_in_single_message_deduplicated(self):
        message = (
            "https://www.instagram.com/reel/C7xyz123/?igsh=1 "
            "again https://www.instagram.com/reel/C7xyz123/?igsh=2"
        )
        expected = ["https://www.kkclip.com/reel/C7xyz123"]
        assert transform_urls(message) == expected

    def test_irrelevant_urls_ignored(self):
        message = "Watch this https://www.youtube.com/watch?v=dQw4w9WgXcQ or read https://x.com/status/1"
        assert transform_urls(message) == []

    def test_plain_text_without_links(self):
        message = "Good morning everyone, remember to post your links later."
        assert transform_urls(message) == []

    def test_bare_root_domain_without_content_path(self):
        message = "Visit https://www.instagram.com/ today"
        assert transform_urls(message) == []


class TestMessageFormatting:
    """Tests verify Discord masked link formatting."""

    def test_format_single_link(self):
        links = ["https://www.kkclip.com/reel/C7xyz123"]
        expected = "[Fixed Embed](https://www.kkclip.com/reel/C7xyz123)"
        assert format_message(links) == expected

    def test_format_multiple_links(self):
        links = [
            "https://www.kkclip.com/reel/C7xyz123",
            "https://www.kkclip.com/@user/video/9876543210",
        ]
        expected = (
            "[Fixed Embed](https://www.kkclip.com/reel/C7xyz123)\n"
            "[Fixed Embed](https://www.kkclip.com/@user/video/9876543210)"
        )
        assert format_message(links) == expected

    def test_format_empty_links(self):
        assert format_message([]) == ""

