import unittest

from ai_engine import extract_chapter_word_target


class TestExtractChapterWordTarget(unittest.TestCase):

    def test_empty_plan_returns_default_target(self):

        result = extract_chapter_word_target(
            "",
            default_target=3000,
        )

        self.assertEqual(
            result,
            3000,
        )

    def test_none_plan_returns_default_target(self):

        result = extract_chapter_word_target(
            None,
            default_target=3000,
        )

        self.assertEqual(
            result,
            3000,
        )

    def test_extracts_approximate_word_target(self):

        chapter_plan = (
            "Approximate Word Target: 3,500 words"
        )

        result = extract_chapter_word_target(
            chapter_plan,
            default_target=3000,
        )

        self.assertEqual(
            result,
            3500,
        )

    def test_extracts_target_word_count(self):

        chapter_plan = (
            "Target Word Count: 4,200"
        )

        result = extract_chapter_word_target(
            chapter_plan,
            default_target=3000,
        )

        self.assertEqual(
            result,
            4200,
        )

    def test_out_of_range_target_returns_default(self):

        chapter_plan = (
            "Approximate Word Target: 20,000 words"
        )

        result = extract_chapter_word_target(
            chapter_plan,
            default_target=3000,
        )

        self.assertEqual(
            result,
            3000,
        )

    def test_unrecognized_text_returns_default(self):

        chapter_plan = (
            "Write a strong chapter with escalating tension."
        )

        result = extract_chapter_word_target(
            chapter_plan,
            default_target=3000,
        )

        self.assertEqual(
            result,
            3000,
        )


if __name__ == "__main__":

    unittest.main()