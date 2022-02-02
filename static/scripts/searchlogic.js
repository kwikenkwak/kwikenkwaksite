console.log("hello world");

var searchbar = document.getElementById("searchbar");
var sortOpt = "Newest";
var viewOpt = "All";
var searchText = "";

searchbar.addEventListener('input', adjustSearch);

function adjustSearch(e){
  searchText = e.target.value.toLowerCase();
  updatePostVisibility();
}

function updatePostVisibility(){
  postItems = document.getElementsByClassName("post-item");
  for(let i = 0; i < postItems.length; i++){
    if(postItems[i].getAttribute('data-title').toLowerCase().includes(searchText) &&
        (viewOpt == "All" || (
          postItems[i].getAttribute('data-type') == "image" && viewOpt == "Images" ||
          postItems[i].getAttribute('data-type') == "video" && viewOpt == "Videos")
        )
      )
      postItems[i].style.display = "block";
    else
      postItems[i].style.display = "none";
  }

}

var sortOptionButtons = document.getElementsByClassName("sort-option");

for(let i = 0; i < sortOptionButtons.length; i++){
  sortOptionButtons[i].addEventListener('click', changeSortOption)
}

function changeSortOption(e){
  sortOpt = e.target.innerHTML.trim();
  var currentSortOptButton = document.getElementById("sort-option-selected");
  var oldSortOpt = currentSortOptButton.innerHTML;
  e.target.innerHTML = oldSortOpt;
  currentSortOptButton.innerHTML = sortOpt;
  updateSortOpt();
  }

function updateSortOpt(){
  var postItems = Array.from(document.getElementsByClassName("post-item"));
  if(sortOpt == "Newest")
    postItems.sort(newestSort);
  else if(sortOpt == "Oldest")
    postItems.sort(oldestSort);
  else
    postItems.sort(alphabeticSort);
  for(let i = 0; i < postItems.length; i++){
    postItems[i].style.order = postItems.indexOf(postItems[i]);
  }
}

function newestSort(a, b){
  var dataA = a.getAttribute("data-date");
  var dataB = b.getAttribute("data-date");
  return dataA < dataB;
}

function oldestSort(a, b){
  var dataA = a.getAttribute("data-date");
  var dataB = b.getAttribute("data-date");
  console.log(dataA);
  return dataA > dataB;
}

function alphabeticSort(a, b){
  var titleA = a.getAttribute("data-title").toLowerCase();
  var titleB = b.getAttribute("data-title").toLowerCase();
  return titleA > titleB;
}

var clearButton = document.getElementById("searchclear");
clearButton.addEventListener('click', clearSearch);

function clearSearch(){
  searchbar.value = "";
  searchText = "";
  updatePostVisibility();
}




var viewOptionButtons = document.getElementsByClassName("view-option");

for(let i = 0; i < viewOptionButtons.length; i++){
  viewOptionButtons[i].addEventListener('click', changeViewOption)
}

function changeViewOption(e){
  console.log("hoi");
  viewOpt = e.target.textContent.trim();
  var currentViewOptButton = document.getElementById("view-option-selected");
  var oldViewOpt = currentViewOptButton.textContent;
  e.target.innerHTML = oldViewOpt;
  currentViewOptButton.innerHTML = viewOpt;
  updatePostVisibility();
}

updatePostVisibility();
updateSortOpt();
