#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int i, n, x, sum = 0;
    int arr[100];
    int nguyen[100];
    cout << "Nhap n: ";
    cin >> n;
    while (n <= 0 || n >= 100){
        cout << "n out of range, rewrite: ";
        cin >> n;
    }
    for (i = 0; i < n; i++){
        cout << "Nhap gia tri thu ";
        cout << i + 1;
        cout << ": ";
        cin >> arr[i];
    }
    cout << "Mang: ";
    for (i = 0; i < n; i++){
    	cout << " ";
    	cout << arr[i];
	}
	cout << endl;
	for (i = 0; i < n; i++){
		int count = 0;
		for (int j = 2; j <= sqrt(abs(arr[i]));j++){
			if (arr[i] % j == 0){
				count++;
			}
		}
		if (count == 0){
			nguyen[i] = arr[i];
		}
		else {
			nguyen[i] = 0;
		}
		
	}
	while(true){
		cout << endl;
		cout << "Nhap gia tri X: ";
		cin >> x;
		for (i = 0; i < n; i++){
			sum += nguyen[i];
		}
		while (sum < x){
			cout << "Khong co so thoa man, nhap lai x: ";
			cin >> x;
		}
		cout << "Mang nguyen: ";
		for (i = 0; i < n; i++){
			if (nguyen[i] != 0){
				cout << nguyen[i];
				cout << " ";
			}
		}
    }
}

