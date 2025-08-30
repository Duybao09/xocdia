<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Nhận mã xác nhận</title>
</head>
<body style="font-family: Arial; text-align:center; padding:50px;">
  <h2>🎁 Đây là mã xác nhận của bạn</h2>
  <h1 id="code" style="color:blue;"></h1>
  <p>👉 Hãy copy mã này và nhập vào bot bằng lệnh <b>/nhapma &lt;mã&gt;</b></p>
  <script>
    const urlParams = new URLSearchParams(window.location.search);
    document.getElementById("code").innerText = urlParams.get("code") || "Không có mã";
  </script>
</body>
</html>