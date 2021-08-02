class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Solution #1
        res, shift = 0, 31
        while(n):
            LeastSignificantBit = (n & 1)
            res += (LeastSignificantBit << shift)
            shift -= 1
            n >>= 1
        return res
        """
        
        #Solution #2
        #Mask -> using "AND" to divide n by 2
        #Shift -> using ">>" or "<<"
        #Combine -> using "OR" or "XOR"
        
        # ..:: Step #0 ::..
        # n = abcdefgh
        # Note: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' are not hex representation.
        #       Those are just block names. Every letter represents a block with 4 bits.
        n = (n >> 16) ^ (n << 16)
        # ..:: Step #1 ::..
        # Mask -> not required because we have only two blocks
        #------------------
        # Shift -> (n >> 16) = 0000abcd
        #          (n << 16) = efgh0000
        #------------------
        # Combine -> 0000abcd
        #            efgh0000
        #         XOR--------
        #            efghabcd       
        n = ( (n & 0xff00ff00) >> 8 ) ^ ( (n & 0x00ff00ff) << 8 )
        # ..:: Step #2 ::..
        # Mask -> (n & 0xff00ff00) = ef00ab00
        #         (n & 0x00ff00ff) = 00gh00cd
        #------------------
        # Shift -> (n & 0xff00ff00) >> 8 = 00ef00ab
        #          (n & 0x00ff00ff) << 8 = gh00cd00
        #------------------
        # Combine -> 00ef00ab
        #            gh00cd00
        #         XOR--------
        #            ghefcdab    
        n = ( (n & 0xf0f0f0f0) >> 4 ) ^ ( (n & 0x0f0f0f0f) << 4 )
        # ..:: Step #3 ::..
        # Mask -> (n & 0xf0f0f0f0) = g0e0c0a0
        #         (n & 0x0f0f0f0f) = 0h0f0d0b
        #------------------
        # Shift -> (n & 0xf0f0f0f0) >> 4 = 0g0e0c0a
        #          (n & 0x0f0f0f0f) << 4 = h0f0d0b0
        #------------------
        # Combine -> 0g0e0c0a
        #            h0f0d0b0
        #         XOR--------
        #            hgfedcba    
        n = ( (n & 0xcccccccc) >> 2 ) ^ ( (n & 0x33333333) << 2 )
        # ..:: Step #4 ::..
        # Note: Before reading Step #4, please take a look at the note on Step #0.
        #       'a' = 1234
        #       'b' = 1234
        #       'c' = 1234
        #       'd' = 1234
        #       'e' = 1234
        #       'f' = 1234
        #       'g' = 1234
        #       'h' = 1234
        #       '.' = Seperate blocks for every 4 bits. This is added to improve readability of 32 bits.
        #       Please look above, every integer represents a block with 1 bits.
        #
        # Mask -> 'c' represents "1100" in 4 bit.
        #         '3' represents "0011" in 4 bit.
        #         n = hgfedcba = 1234.1234.1234.1234.1234.1234.1234.1234
        #         (n & 0xcccccccc) = 1234.1234.1234.1234.1234.1234.1234.1234
        #                            1100.1100.1100.1100.1100.1100.1100.1100
        #                         AND---------------------------------------
        #                            1200.1200.1200.1200.1200.1200.1200.1200
        #     
        #         (n & 0x33333333) = 1234.1234.1234.1234.1234.1234.1234.1234
        #                            0011.0011.0011.0011.0011.0011.0011.0011
        #                         AND---------------------------------------
        #                            0034.0034.0034.0034.0034.0034.0034.0034
        #------------------
        # Shift -> (n & 0xcccccccc) >> 2 = 0012.0012.0012.0012.0012.0012.0012.0012
        #          (n & 0x33333333) << 2 = 3400.3400.3400.3400.3400.3400.3400.3400
        #------------------
        # Combine -> 0012.0012.0012.0012.0012.0012.0012.0012
        #            3400.3400.3400.3400.3400.3400.3400.3400
        #         XOR---------------------------------------
        #            3412.3412.3412.3412.3412.3412.3412.3412 
        n = ( (n & 0xaaaaaaaa) >> 1 ) ^ ( (n & 0x55555555) << 1 )
        # ..:: Step #5 ::..
        # Note: Before reading Step #5, please take a look at notes on Step #0 and Step#4.
        #
        # Mask -> 'a' represents "1010" in 4 bit.
        #         '5' represents "0101" in 4 bit.
        #         n = 3412.3412.3412.3412.3412.3412.3412.3412
        #         (n & 0xaaaaaaaa) = 3412.3412.3412.3412.3412.3412.3412.3412
        #                            1010.1010.1010.1010.1010.1010.1010.1010
        #                         AND---------------------------------------
        #                            3010.3010.3010.3010.3010.3010.3010.3010
        #     
        #         (n & 0x55555555) = 3412.3412.3412.3412.3412.3412.3412.3412
        #                            0101.0101.0101.0101.0101.0101.0101.0101
        #                         AND---------------------------------------
        #                            0402.0402.0402.0402.0402.0402.0402.0402
        #------------------
        # Shift -> (n & 0xaaaaaaaa) >> 1 = 0301.0301.0301.0301.0301.0301.0301.0301
        #          (n & 0x55555555) << 1 = 4020.4020.4020.4020.4020.4020.4020.4020
        #------------------
        # Combine -> 0301.0301.0301.0301.0301.0301.0301.0301
        #            4020.4020.4020.4020.4020.4020.4020.4020
        #         XOR---------------------------------------
        #            4321.4321.4321.4321.4321.4321.4321.4321
        return n
        