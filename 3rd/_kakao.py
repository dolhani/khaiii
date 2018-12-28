# -*- coding: utf-8 -*-
import khaiii

__all__ = ['Kakao']


class Kakao():
    """Wrapper for kakao khaiii morphological analyzer.

    `khaiii`_, Kakao Hangul Analyzer III

    .. code-block:: python
        :emphasize-lines: 1

        >>> # khaiii installation needed
        >>> from konlpy.tag import Kakao
        >>> kakao = Kakao()
        >>> print(kakao.morphs(u'우왕 khaiii 오픈소스가 되었어요'))
        ['우왕', 'khaiii', '오픈', '소', '스', '가', '되', '었', '어요']
        >>> print(kakao.nouns(u'우리나라에는 무릎 치료를 잘하는 정형외과가 없는가!'))
        ['우리나라', '무릎', '치료', '정형', '외과']
        >>> print(kakao.pos(u'자연주의 쇼핑몰은 어떤 곳인가?'))
        [('자연주의', 'NNG'), ('쇼핑몰', 'NNG'), ('은', 'JX'), ('어떤', 'MM'), ('곳', 'NNG'), ('이', 'VCP'), ('ㄴ가', 'EF'), ('?', 'SF')]

    .. _khiiii: https://github.com/kakao/khaiii
    """

    def pos(self, phrase, flatten=True, join=False):
        """POS tagger.

        :param flatten: If False, preserves eojeols.
        :param join: If True, returns joined sets of morph and tag.
        """

        sentences = phrase.split('\n')
        morphemes = []
        if not sentences:
            return morphemes

        for sentence in sentences:
            if not sentence:
                continue
            result = self.api.analyze(sentence)
            #result = [(token.getMorph(), token.getPos()) for token in result]
            tmp_result = []
            for token in result:
                tmp_result += [(m.lex, m.tag) for m in token.morphs]
            result = tmp_result

            if join:
                result = ['{}/{}'.format(morph, pos) for morph, pos in result]

            morphemes.append(result)

        if flatten:
            return sum(morphemes, [])
        return morphemes


    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('NN') or t.startswith('SL') or t.startswith('SH') or t.startswith('NF')]

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]


    def __init__(self):
        self.api = khaiii.KhaiiiApi()
        self.api.open()
