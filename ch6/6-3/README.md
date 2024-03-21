Assume we only have lowercase alphabets<br/>
The expected compression ratio in (a) is $(str\_len * 8) / \lceil str\_len * log2(26) \rceil$. <br/> 
Each character counts $log2(26)$ bits of information. However, the program has integer value of bits. Therefore, we have the ceil of $str\_len * log2(26)$ as the length of encoded bit length.