#!/usr/bin/env python

import unittest


class TestComplexMethod( unittest.TestCase):
    def test_complex(self):
        z = 4.7 + 0.66j
        self.assertEqual( z.real, 4.7 )
        self.assertEqual( z.imag, 0.66 )
        self.assertEqual( z, 4.7+0.66j )


if __name__ == '__main__':
   unittest.main()
