{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNXMhoVDzXbWdWjqnIwz4S6"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Latihan 6"],"metadata":{"id":"RFgYPOOzQBVS"}},{"cell_type":"code","execution_count":3,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"wkIOcwegP2a8","executionInfo":{"status":"ok","timestamp":1701533142205,"user_tz":480,"elapsed":449,"user":{"displayName":"Meiana Sahabuddin","userId":"14158662633177642352"}},"outputId":"71801bb8-4abb-47ea-d492-feced82843c4"},"outputs":[{"output_type":"stream","name":"stdout","text":["Fibonacci(20) = 6765\n"]}],"source":["#Fungsi Rekursif Fibonacci\n","def fibonacci(n):\n","  if n<0:\n","    print('Tidak ada bilangan yang bernilai negatif')\n","  if n==0 or n==1:\n","    return n\n","  else:\n","    return fibonacci(n - 1) + fibonacci(n - 2)\n","\n","#Program utama\n","hasil=fibonacci(20)\n","print('Fibonacci(%d) = %d' % (20,hasil))"]},{"cell_type":"markdown","source":["Tugas (Buatlah program dengan output sebagai berikut (ket: gunakan input sebagai masukan, 20 merupakan input))"],"metadata":{"id":"j2d2ntV3R6GN"}},{"cell_type":"code","execution_count":45,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1701535873479,"user_tz":480,"elapsed":4665,"user":{"displayName":"Meiana Sahabuddin","userId":"14158662633177642352"}},"outputId":"a88e6169-ccbf-41f8-d257-c27aff66ceda","id":"9907U83JScMF"},"outputs":[{"output_type":"stream","name":"stdout","text":["Masukkan Sebuah Bilangan: 20\n","Fibonacci(20) = 6765\n"]}],"source":["\n","def fibonacci(n):\n","  if n<0:\n","    print('Tidak ada bilangan yang bernilai negatif')\n","  if n==0 or n==1:\n","    return n\n","  else:\n","    return fibonacci(n - 1) + fibonacci(n - 2)\n","\n","#Program utama\n","nilai = int(input(\"Masukkan Sebuah Bilangan: \"))\n","hasil=fibonacci(nilai)\n","print('Fibonacci(%d) = %d' % (nilai,hasil))"]}]}