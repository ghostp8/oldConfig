let mapleader=" "



syntax on

set clipboard+=unnamedplus

set noerrorbells


set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch

set mouse=a
set number relativenumber
set termguicolors
" colorscheme codedark

" autocompletion doesent seem to work
set wildmode=longest,list,full

" fix splitting
set splitbelow splitright




" line and colume highlighting
set cursorline
"set cursorcolumn
highlight CursorLine ctermbg=Yellow cterm=bold guibg=#2b2b2b
"highlight CursorColumn ctermbg=Yellow cterm=bold guibg=#2b2b2b

autocmd InsertEnter * norm zz
autocmd BufWritePre * %s/\s\+$//e



" change auto comment
map <leader>c :setlocal formatoptions-=cro<CR>
map <leader>C :setlocal formatoptions=cro<CR>

" change auto indent
map <leader>i :setlocal autoindent<CR>
map <leader>I :setlocal noautoindent<CR>



" remap split change
map <C-h> <C-w>h
map <C-j> <c-w>j
map <C-k> <c-w>k
map <C-l> <c-w>l



" Alias replace all to S
nnoremap S :%s///gI<Left><Left><Left>



