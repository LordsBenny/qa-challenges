import pytest
from question1.main import generate_pyramid


@pytest.mark.parametrize(
    "n, char, expected",
    [
        (-1, "!", ""),
        (0, "@", ""),
        (1, "#", "#\n"),
        (2, "$", " $\n$$$\n"),
        (3, "#", "  #\n ###\n#####\n"),
        (4, "%", "   %\n  %%%\n %%%%%\n%%%%%%%\n"),
        (5, "*", "    *\n   ***\n  *****\n *******\n*********\n"),
        (6, "^", "     ^\n    ^^^\n   ^^^^^\n  ^^^^^^^\n ^^^^^^^^^\n^^^^^^^^^^^\n"),
        (7, "&", "      &\n     &&&\n    &&&&&\n   &&&&&&&\n  &&&&&&&&&\n &&&&&&&&&&&\n&&&&&&&&&&&&&\n"),
        (8, "a", "       a\n      aaa\n     aaaaa\n    aaaaaaa\n   aaaaaaaaa\n  aaaaaaaaaaa\n aaaaaaaaaaaaa\naaaaaaaaaaaaaaa\n"),
        (9, "b", "        b\n       bbb\n      bbbbb\n     bbbbbbb\n    bbbbbbbbb\n   bbbbbbbbbbb\n  bbbbbbbbbbbbb\n bbbbbbbbbbbbbbb\nbbbbbbbbbbbbbbbbb\n"),
        (10, "L", "         L\n        LLL\n       LLLLL\n      LLLLLLL\n     LLLLLLLLL\n    LLLLLLLLLLL\n   LLLLLLLLLLLLL\n  LLLLLLLLLLLLLLL\n LLLLLLLLLLLLLLLLL\nLLLLLLLLLLLLLLLLLLL\n"),
        (11, "r", "          r\n         rrr\n        rrrrr\n       rrrrrrr\n      rrrrrrrrr\n     rrrrrrrrrrr\n    rrrrrrrrrrrrr\n   rrrrrrrrrrrrrrr\n  rrrrrrrrrrrrrrrrr\n rrrrrrrrrrrrrrrrrrr\nrrrrrrrrrrrrrrrrrrrrr\n"),
        (12, "d", "           d\n          ddd\n         ddddd\n        ddddddd\n       ddddddddd\n      ddddddddddd\n     ddddddddddddd\n    ddddddddddddddd\n   ddddddddddddddddd\n  ddddddddddddddddddd\n ddddddddddddddddddddd\nddddddddddddddddddddddd\n"),
        (13, "T", "            T\n           TTT\n          TTTTT\n         TTTTTTT\n        TTTTTTTTT\n       TTTTTTTTTTT\n      TTTTTTTTTTTTT\n     TTTTTTTTTTTTTTT\n    TTTTTTTTTTTTTTTTT\n   TTTTTTTTTTTTTTTTTTT\n  TTTTTTTTTTTTTTTTTTTTT\n TTTTTTTTTTTTTTTTTTTTTTT\nTTTTTTTTTTTTTTTTTTTTTTTTT\n"),
        (14, "F", "             F\n            FFF\n           FFFFF\n          FFFFFFF\n         FFFFFFFFF\n        FFFFFFFFFFF\n       FFFFFFFFFFFFF\n      FFFFFFFFFFFFFFF\n     FFFFFFFFFFFFFFFFF\n    FFFFFFFFFFFFFFFFFFF\n   FFFFFFFFFFFFFFFFFFFFF\n  FFFFFFFFFFFFFFFFFFFFFFF\n FFFFFFFFFFFFFFFFFFFFFFFFF\nFFFFFFFFFFFFFFFFFFFFFFFFFFF\n"),
        (15, "Y", "              Y\n             YYY\n            YYYYY\n           YYYYYYY\n          YYYYYYYYY\n         YYYYYYYYYYY\n        YYYYYYYYYYYYY\n       YYYYYYYYYYYYYYY\n      YYYYYYYYYYYYYYYYY\n     YYYYYYYYYYYYYYYYYYY\n    YYYYYYYYYYYYYYYYYYYYY\n   YYYYYYYYYYYYYYYYYYYYYYY\n  YYYYYYYYYYYYYYYYYYYYYYYYY\n YYYYYYYYYYYYYYYYYYYYYYYYYYY\nYYYYYYYYYYYYYYYYYYYYYYYYYYYYY\n"),
        (16, "I", "               I\n              III\n             IIIII\n            IIIIIII\n           IIIIIIIII\n          IIIIIIIIIII\n         IIIIIIIIIIIII\n        IIIIIIIIIIIIIII\n       IIIIIIIIIIIIIIIII\n      IIIIIIIIIIIIIIIIIII\n     IIIIIIIIIIIIIIIIIIIII\n    IIIIIIIIIIIIIIIIIIIIIII\n   IIIIIIIIIIIIIIIIIIIIIIIII\n  IIIIIIIIIIIIIIIIIIIIIIIIIII\n IIIIIIIIIIIIIIIIIIIIIIIIIIIII\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n"),
        (17, "z", "                z\n               zzz\n              zzzzz\n             zzzzzzz\n            zzzzzzzzz\n           zzzzzzzzzzz\n          zzzzzzzzzzzzz\n         zzzzzzzzzzzzzzz\n        zzzzzzzzzzzzzzzzz\n       zzzzzzzzzzzzzzzzzzz\n      zzzzzzzzzzzzzzzzzzzzz\n     zzzzzzzzzzzzzzzzzzzzzzz\n    zzzzzzzzzzzzzzzzzzzzzzzzz\n   zzzzzzzzzzzzzzzzzzzzzzzzzzz\n  zzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n"),
        (18, "I", "                 I\n                III\n               IIIII\n              IIIIIII\n             IIIIIIIII\n            IIIIIIIIIII\n           IIIIIIIIIIIII\n          IIIIIIIIIIIIIII\n         IIIIIIIIIIIIIIIII\n        IIIIIIIIIIIIIIIIIII\n       IIIIIIIIIIIIIIIIIIIII\n      IIIIIIIIIIIIIIIIIIIIIII\n     IIIIIIIIIIIIIIIIIIIIIIIII\n    IIIIIIIIIIIIIIIIIIIIIIIIIII\n   IIIIIIIIIIIIIIIIIIIIIIIIIIIII\n  IIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n"),
        (19, "U", "                  U\n                 UUU\n                UUUUU\n               UUUUUUU\n              UUUUUUUUU\n             UUUUUUUUUUU\n            UUUUUUUUUUUUU\n           UUUUUUUUUUUUUUU\n          UUUUUUUUUUUUUUUUU\n         UUUUUUUUUUUUUUUUUUU\n        UUUUUUUUUUUUUUUUUUUUU\n       UUUUUUUUUUUUUUUUUUUUUUU\n      UUUUUUUUUUUUUUUUUUUUUUUUU\n     UUUUUUUUUUUUUUUUUUUUUUUUUUU\n    UUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n   UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n  UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\nUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n"),
        (20, "M", "                   M\n                  MMM\n                 MMMMM\n                MMMMMMM\n               MMMMMMMMM\n              MMMMMMMMMMM\n             MMMMMMMMMMMMM\n            MMMMMMMMMMMMMMM\n           MMMMMMMMMMMMMMMMM\n          MMMMMMMMMMMMMMMMMMM\n         MMMMMMMMMMMMMMMMMMMMM\n        MMMMMMMMMMMMMMMMMMMMMMM\n       MMMMMMMMMMMMMMMMMMMMMMMMM\n      MMMMMMMMMMMMMMMMMMMMMMMMMMM\n     MMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"),
        (21, "x", "                    x\n                   xxx\n                  xxxxx\n                 xxxxxxx\n                xxxxxxxxx\n               xxxxxxxxxxx\n              xxxxxxxxxxxxx\n             xxxxxxxxxxxxxxx\n            xxxxxxxxxxxxxxxxx\n           xxxxxxxxxxxxxxxxxxx\n          xxxxxxxxxxxxxxxxxxxxx\n         xxxxxxxxxxxxxxxxxxxxxxx\n        xxxxxxxxxxxxxxxxxxxxxxxxx\n       xxxxxxxxxxxxxxxxxxxxxxxxxxx\n      xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    ]
)
def test_generate_pyramid(n, char, expected):
    assert generate_pyramid(n, char) == expected
