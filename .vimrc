"echo "~/.vimrc loaded!"

" For better pasting,  type -> :set paste
" to return to normal, type -> :set nopaste

filetype on
filetype plugin indent on

" Colorful text
syntax on

" Show number lines
set number
"set relativenumber

"-------- Indentation ----------
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

" Start Gundo, the graphical way to search undo tree
nnoremap <F5> :GundoToggle<CR>

" yank to end of line
map Y y$

" move to end of line
map E $

" move to begining of line
map B ^

map j gj
map k gk

" navegate between windows using Ctrl (h,j,k,l)
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
"------------------------------ 

" Enables use of mouse
set mouse=a

" Tab in command mode to show options/autocomplete
set wildmenu

" Javascript from https://github.com/pangloss/vim-javascript
let g:javascript_enable_domhtmlcss = 1
let g:javascript_ignore_javaScriptdoc = 1
"set foldmethod=syntax
"
