import struct

def tamper(student_id): 
  with open('lenna.bmp','r+b') as stuid:
    num = str(student_id)
    bg = int(54)
    stuid.seek(bg)
    for a in num:
          n = int(a)
          if(n != 0):
                bg =bg + n*3
          else:
                bg =bg + 10*3
          stuid.seek(bg-3)
          stuid.read(3)
          stuid.write(b'\x00\x00\x00')
  stuid.close()

def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
