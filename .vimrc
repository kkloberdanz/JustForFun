"echo "~/.vimrc loaded!"

" For better pasting, type  -> :set paste
" to return to normal, type -> :set nopaste

filetype on

" Colorful text
syntax on

"set number

"-------- Indentation ----------
filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab 
set autoindent
"------------------------------

" Starts pathogen
execute pathogen#infect()

"------- Custom mapping ------- 
" Start NERDTree with CTRL+n
map <C-n> :NERDTreeToggle<CR>
map Y y$
"------------------------------ 

" Enables use of mouse
set mouse=a
