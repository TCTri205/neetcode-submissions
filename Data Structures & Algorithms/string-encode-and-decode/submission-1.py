class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Tìm vị trí dấu '#' phân tách độ dài
            j = i
            while s[j] != "#":
                j += 1
            
            # Đọc độ dài của chuỗi tiếp theo
            length = int(s[i:j])
            
            # Cắt lấy chuỗi con dựa vào độ dài
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Di chuyển con trỏ i đến vị trí bắt đầu của từ kế tiếp
            i = j + 1 + length
            
        return res