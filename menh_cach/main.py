thien_can = ["giáp", "ất", "bính", "đinh","mậu","kỷ","canh","tân","nhâm","quý"]
dia_chi = ["tý", "sửu", "dần", "mẹo", "thìn", "tỵ", "ngọ", "mùi", "thân", "dậu", "tuất", "hợi"]
menh_cach = ["Kim", "Thủy", "Hỏa", "Thổ", "Mộc", "Kim", "Thủy"]
menh_ngu_hanh = [
    "Thạch lựu mộc (Cây thạch lựu)", \
    "Đại hải thủy (Nước đại dương)", \
    "Hải trung kim (Vàng dưới biển)", \
    "Lộ trung hỏa (Lửa trong lò)", \
    "Đại lâm mộc (Cây trong rừng lớn)", \
    "Lộ bàng thổ (Đất giữa đường)", \
    "Kiếm phong kim (Vàng đầu mũi kiếm)", \
    "Sơn đầu hỏa (Lửa trên núi)", \
    "Giản hạ thủy (Nước dưới khe)", \
    "Thành đầu thổ (Đất trên thành)", \
    "Bạch lạp kim (Vàng trong nến rắn)", \
    "Dương liễu mộc (Cây dương liễu)", \
    "Tuyền trung thủy (Dưới giữa dòng suối)", \
    "Ốc thượng thổ (Đất trên nóc nhà)", \
    "Tích Lịch Hỏa (Lửa sấm sét)", \
    "Tùng bách mộc (Cây tùng bách)" , \
    "Trường lưu thủy (Giòng nước lớn)" , \
    "Sa trung kim (Vàng trong cát)", \
    "Sơn hạ hỏa (Lửa dưới chân núi)", \
    "Bình địa mộc (Cây ở đồng bằng)", \
    "Bích thượng thổ (Đất trên vách)", \
    "Kim bạch kim (Vàng pha bạch kim)", \
    "Phú đăng hỏa (Lửa đèn dầu)", \
    "Thiên hà thủy (Nước trên trời)", \
    "Đại dịch thổ (Đất thuộc 1 khu lớn)", \
    "Thoa xuyến kim (Vàng trang sức)", \
    "Tang đố mộc (Gỗ cây dâu)", \
    "Đại khê thủy (Nước dưới khe lớn)", \
    "Sa trung thổ (Đất lẫn trong cát)", \
    "Thiên thượng hỏa (Lửa trên trời)"
]
def tinh_menh(can, chi):
    so_thien_can = int((can + 1)%2) + int((can + 1)/2)
    so_dia_chi = int((chi + 1)%2 + (chi + 1)/2 - 1) \
                    if (chi + 1) <= 6 \
                    else int((chi - 5)%2 + (chi - 5)/2 - 1)
    # print(so_thien_can)
    # print(so_dia_chi)
    return menh_cach[so_thien_can + so_dia_chi - 1]
def thien_can_dia_chi(year):
    can = int(year%10) - 4 if int(year%10) >= 4 else int(year%10) + 6
    # print(can)
    chi = int(year%12) - 4 if int(year%12) >= 4 else int(year%12) + 8
    # print(chi)
    ngu_hanh_menh = menh_ngu_hanh[int((year%60)/2)]
    return can, chi, ngu_hanh_menh

def chuoi_nam(start, end):
    for i in range(start, end):
        can, chi, ngu_hanh_menh = thien_can_dia_chi(i)
        so_menh = tinh_menh(can, chi)
        print ("Mệnh " + str(i) + " " + thien_can[can] + " " + dia_chi[chi] + " : " + so_menh + " \" " + ngu_hanh_menh  + " \" ")

def mot_nam(year):
    can, chi, ngu_hanh_menh = thien_can_dia_chi(year)
    so_menh = tinh_menh(can, chi)
    print ("Mệnh " + str(year) + " " + thien_can[can] + " " + dia_chi[chi] + " : " + so_menh + " \" " + ngu_hanh_menh  + " \" ")

def main():
    chuoi_nam(2020, 2040)
    
if __name__ == "__main__":
    main()