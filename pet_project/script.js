let cartCount = 0;
const cartIcon = document.getElementById("cartIcon");
const cartCountSpan = document.getElementById("cartCount");
const searchBtn = document.getElementById("searchBtn");

cartIcon.addEventListener("click", () => {
  cartCount++;
  cartCountSpan.textContent = cartCount;
  alert("Đã thêm sản phẩm vào giỏ!");
});

searchBtn.addEventListener("click", () => {
  const query = document.getElementById("searchInput").value;
  if (query.trim()) {
    alert(`Tìm kiếm: ${query}`);
  }
});
