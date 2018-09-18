def solution(s)
  list = s.split("\n")

  list.map! do |photo|
    photo.split(",")
  end

  cities = Hash.new()

  list.each do |photo|
    if cities[photo[1]] == nil
      cities[photo[1]] = []
      cities[photo[1]] << photo
    else
      cities[photo[1]] << photo
    end
  end

  cities.keys.each do |city|
    cities[city].sort_by! {|photo| photo[-1]}
  end

  list.map! do |photo|
    city_photos = cities[photo[1]]
    total_photos = city_photos.length
    city_photos = city_photos.map {|photo| photo.join("")}
    time = photo[-1]
    city = photo[1]
    file_type = which_format(photo[0])
    idx = city_photos.index(photo.join("")) + 1
    city + number(idx, total_photos) + file_type
  end

  return list.join("\n")
end


def which_format(s)
  return ".jpg" if s.include?("jpg")
  return ".png" if s.include?("png")
  return ".jpeg" if s.include?("jpeg")
end

def number(i, length)
  num_zeros = length.to_s.length - i.to_s.length
  zeroes = ""
  num_zeros.times {zeroes += "0"}
  return zeroes + i.to_s
end

s = "photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"

p solution(s)
