const btnDelete = document.querySelectorAll('.btn-delete')
/*
Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
      'Deleted!',
      'Your file has been deleted.',
      'success'
    )
  }
})
*/
if(btnDelete){
  const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
      btn.addEventListener('click', (e) =>{
        if(!confirm('Are you sure you want to delete it?')){
            e.preventDefault();
          }
        })
    })
}
