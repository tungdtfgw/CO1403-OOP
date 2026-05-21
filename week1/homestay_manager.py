# sử dụng từ điển để quản lý homestay
# các phòng đều đang trống, nên value của các key là chuỗi rỗng
rooms = {
    '101': '',
    '102': '',
    '103': '',
    '201': '',
    '202': '',
    '203': '',
}   

def homestay_manager():
    running = True

    while running:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_rooms()
        elif choice == 2:
            check_in()
        elif choice == 3:
            check_out()
        elif choice == 4:
            print("Exiting the program.")
            running = False
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print('Homestay Management System')
    print('1. View Rooms')
    print('2. Check In')
    print('3. Check Out')
    print('4. Exit')

def view_rooms():
    # Lặp qua các phòng và in ra thông tin
    print('All Rooms:')
    for room_number, guest in rooms.items():
        if guest == '':
            print(f'Room {room_number}: Empty')
        else:
            print(f'Room {room_number}: {guest}')

def check_in():
    print('New guest check-in')
    room_number = input("Enter room number: ")
    # kiểm tra xem phòng có tồn tại không
    if room_number not in rooms:
        print(f'Room {room_number} does not exist.')
        return
    # kiểm tra xem phòng có đang trống không
    if rooms[room_number] != '':
        print(f'Room {room_number} is currently occupied.')
        return
    
    # cập nhật thông tin khách vào phòng
    guest_name = input("Enter guest name: ")
    rooms[room_number] = guest_name
    print(f'Guest {guest_name} checked into room {room_number} successfully.')

def check_out():
    print('Check out a guest')
    room_number = input("Enter room number: ")
    # kiểm tra xem phòng có tồn tại không
    if room_number not in rooms:
        print(f'Room {room_number} does not exist.')
        return
    # kiểm tra xem phòng có đang trống không
    if rooms[room_number] == '':
        print(f'Room {room_number} is currently empty.')
        return

    # cập nhật thông tin khách ra khỏi phòng
    guest_name = rooms[room_number] # lấy tên khách đang ở trong phòng (truyền vào key => value)
    rooms[room_number] = ''
    print(f'Guest {guest_name} checked out from room {room_number} successfully.')

if __name__ == "__main__":
    homestay_manager()