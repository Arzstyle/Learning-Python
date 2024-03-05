# Program untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya, sesuai dengan input pengguna.

celcius = float(input("Masukan suhu celcius : "))
fahrenheit = float(input("Masukan suhu fahrenheit : "))

rumus_celcius = 5/4 * fahrenheit
rumus_fahrenheit = 9/4 * celcius + 32

print(f"Suhu Celcius {celcius} -> Suhu Fahrenheit {rumus_fahrenheit:.0f} Derajat Fahrenheit ")
print(f"Suhu Fahrenheit {fahrenheit} -> Suhu Celcius {rumus_celcius:.0f} Derajat Fahrenheit")