<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Directory Manager</title>
    <style>
        :root {
            --primary-color: #4a6fa5;
            --secondary-color: #166088;
            --accent-color: #4fc3f7;
            --background-color: #f5f7fa;
            --card-color: #ffffff;
            --text-color: #333333;
            --border-color: #e0e0e0;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
        }

        h1 {
            color: var(--primary-color);
            font-size: 28px;
        }

        .ai-tag {
            background-color: var(--accent-color);
            color: white;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 12px;
            margin-left: 10px;
        }

        .search-container {
            position: relative;
            width: 400px;
        }

        #search-input {
            width: 100%;
            padding: 12px 20px;
            border: 1px solid var(--border-color);
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        #search-input:focus {
            border-color: var(--accent-color);
            box-shadow: 0 2px 10px rgba(79, 195, 247, 0.3);
        }

        #search-results {
            position: absolute;
            width: 100%;
            max-height: 300px;
            overflow-y: auto;
            background-color: var(--card-color);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            margin-top: 5px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            z-index: 100;
            display: none;
        }

        .search-result-item {
            padding: 10px 15px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .search-result-item:hover {
            background-color: var(--background-color);
        }

        .search-result-item .path {
            font-size: 12px;
            color: #666;
            margin-top: 3px;
        }

        .main-content {
            display: flex;
            gap: 20px;
        }

        .sidebar {
            width: 250px;
            background-color: var(--card-color);
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .directory-tree {
            list-style: none;
        }

        .directory-tree li {
            margin-bottom: 5px;
        }

        .directory-tree a {
            display: block;
            padding: 8px 10px;
            color: var(--text-color);
            text-decoration: none;
            border-radius: 5px;
            transition: all 0.2s;
        }

        .directory-tree a:hover {
            background-color: var(--background-color);
            color: var(--primary-color);
        }

        .directory-tree a.active {
            background-color: var(--primary-color);
            color: white;
        }

        .directory-tree .folder {
            font-weight: bold;
        }

        .directory-tree .folder::before {
            content: '📁 ';
        }

        .directory-tree .file::before {
            content: '📄 ';
        }

        .content-area {
            flex: 1;
            background-color: var(--card-color);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .breadcrumb {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
        }

        .breadcrumb a {
            color: var(--primary-color);
            text-decoration: none;
            margin: 0 5px;
        }

        .breadcrumb a:first-child {
            margin-left: 0;
        }

        .breadcrumb a:hover {
            text-decoration: underline;
        }

        .breadcrumb .separator {
            color: #999;
        }

        .file-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 15px;
        }

        .file-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }

        .file-item:hover {
            background-color: var(--background-color);
            transform: translateY(-3px);
        }

        .file-icon {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .file-name {
            font-size: 14px;
            word-break: break-word;
            width: 100%;
        }

        .file-actions {
            display: none;
            margin-top: 10px;
        }

        .file-item:hover .file-actions {
            display: flex;
            gap: 5px;
        }

        .action-btn {
            background: none;
            border: none;
            color: var(--primary-color);
            cursor: pointer;
            font-size: 14px;
            padding: 2px 5px;
            border-radius: 3px;
        }

        .action-btn:hover {
            background-color: rgba(74, 111, 165, 0.1);
        }

        .ai-suggestions {
            margin-top: 30px;
            background-color: rgba(79, 195, 247, 0.1);
            border-radius: 10px;
            padding: 15px;
            border-left: 4px solid var(--accent-color);
        }

        .ai-suggestions h3 {
            color: var(--secondary-color);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }

        .ai-suggestions h3::before {
            content: '💡';
            margin-right: 8px;
        }

        .suggestion-item {
            margin-bottom: 10px;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .suggestion-item:hover {
            background-color: var(--background-color);
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background-color: var(--card-color);
            padding: 25px;
            border-radius: 10px;
            width: 400px;
            max-width: 90%;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .modal-header h2 {
            color: var(--primary-color);
        }

        .close-btn {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #999;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid var(--border-color);
            border-radius: 5px;
            font-size: 16px;
        }

        .modal-actions {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-top: 20px;
        }

        .btn {
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
        }

        .btn-primary {
            background-color: var(--primary-color);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--secondary-color);
        }

        .btn-secondary {
            background-color: var(--border-color);
            color: var(--text-color);
        }

        .btn-secondary:hover {
            background-color: #d0d0d0;
        }

        .status-bar {
            margin-top: 20px;
            padding: 10px;
            background-color: var(--card-color);
            border-radius: 5px;
            font-size: 14px;
            color: #666;
            display: flex;
            justify-content: space-between;
        }

        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }

            .sidebar {
                width: 100%;
            }

            .search-container {
                width: 100%;
                margin-top: 15px;
            }

            header {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Directory Manager <span class="ai-tag">AI Powered</span></h1>
            <div class="search-container">
                <input type="text" id="search-input" placeholder="Search files or ask AI...">
                <div id="search-results"></div>
            </div>
        </header>

        <div class="main-content">
            <div class="sidebar">
                <h3>Directory Tree</h3>
                <ul class="directory-tree" id="directory-tree">
                    <!-- Populated by JavaScript -->
                </ul>
            </div>

            <div class="content-area">
                <div class="breadcrumb" id="breadcrumb">
                    <a href="#" data-path="">Home</a>
                </div>

                <div class="file-grid" id="file-grid">
                    <!-- Populated by JavaScript -->
                </div>

                <div class="ai-suggestions">
                    <h3>AI Suggestions</h3>
                    <div id="suggestions-container">
                        <!-- Populated by JavaScript -->
                    </div>
                </div>
            </div>
        </div>

        <div class="status-bar">
            <div id="status-message">Ready</div>
            <div id="item-count">0 items</div>
        </div>
    </div>

    <!-- New Folder Modal -->
    <div class="modal" id="new-folder-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Create New Folder</h2>
                <button class="close-btn">&times;</button>
            </div>
            <div class="form-group">
                <label for="folder-name">Folder Name</label>
                <input type="text" id="folder-name" placeholder="Enter folder name">
            </div>
            <div class="modal-actions">
                <button class="btn btn-secondary close-btn">Cancel</button>
                <button class="btn btn-primary" id="create-folder-btn">Create</button>
            </div>
        </div>
    </div>

    <!-- Upload File Modal -->
    <div class="modal" id="upload-file-modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Upload File</h2>
                <button class="close-btn">&times;</button>
            </div>
            <div class="form-group">
                <label for="file-upload">Select File</label>
                <input type="file" id="file-upload">
            </div>
            <div class="modal-actions">
                <button class="btn btn-secondary close-btn">Cancel</button>
                <button class="btn btn-primary" id="upload-file-btn">Upload</button>
            </div>
        </div>
    </div>

    <script>
        // Sample directory structure
        const directoryStructure = {
            name: "Root",
            path: "",
            type: "folder",
            children: [
                {
                    name: "Documents",
                    path: "Documents",
                    type: "folder",
                    children: [
                        {
                            name: "Project Proposal.docx",
                            path: "Documents/Project Proposal.docx",
                            type: "file",
                            size: "245 KB",
                            modified: "2023-05-15"
                        },
                        {
                            name: "Budget.xlsx",
                            path: "Documents/Budget.xlsx",
                            type: "file",
                            size: "180 KB",
                            modified: "2023-05-10"
                        }
                    ]
                },
                {
                    name: "Images",
                    path: "Images",
                    type: "folder",
                    children: [
                        {
                            name: "Vacation",
                            path: "Images/Vacation",
                            type: "folder",
                            children: [
                                {
                                    name: "beach.jpg",
                                    path: "Images/Vacation/beach.jpg",
                                    type: "file",
                                    size: "1.2 MB",
                                    modified: "2023-04-22"
                                }
                            ]
                        },
                        {
                            name: "profile.png",
                            path: "Images/profile.png",
                            type: "file",
                            size: "350 KB",
                            modified: "2023-05-01"
                        }
                    ]
                },
                {
                    name: "Code",
                    path: "Code",
                    type: "folder",
                    children: [
                        {
                            name: "index.html",
                            path: "Code/index.html",
                            type: "file",
                            size: "15 KB",
                            modified: "2023-05-18"
                        },
                        {
                            name: "styles.css",
                            path: "Code/styles.css",
                            type: "file",
                            size: "8 KB",
                            modified: "2023-05-18"
                        }
                    ]
                }
            ]
        };

        // AI suggestions based on content
        const aiSuggestions = [
            {
                id: 1,
                title: "Organize by project",
                description: "Your documents seem to be mixed. Would you like to create project-specific folders?",
                action: "organize"
            },
            {
                id: 2,
                title: "Backup old files",
                description: "You have files older than 6 months. Consider archiving them.",
                action: "backup"
            },
            {
                id: 3,
                title: "Duplicate files detected",
                description: "Possible duplicates in Documents and Code folders.",
                action: "cleanup"
            }
        ];

        // Current directory state
        let currentPath = "";
        let currentDirectory = directoryStructure;

        // DOM elements
        const directoryTree = document.getElementById('directory-tree');
        const fileGrid = document.getElementById('file-grid');
        const breadcrumb = document.getElementById('breadcrumb');
        const searchInput = document.getElementById('search-input');
        const searchResults = document.getElementById('search-results');
        const suggestionsContainer = document.getElementById('suggestions-container');
        const statusMessage = document.getElementById('status-message');
        const itemCount = document.getElementById('item-count');

        // Initialize the application
        function init() {
            renderDirectoryTree();
            renderCurrentDirectory();
            renderBreadcrumb();
            renderAiSuggestions();
            setupEventListeners();
        }

        // Render the directory tree in the sidebar
        function renderDirectoryTree() {
            directoryTree.innerHTML = '';
            const renderTree = (node, parentElement) => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = '#';
                a.textContent = node.name;
                a.className = node.type;
                a.setAttribute('data-path', node.path);
                
                if (node.path === currentPath) {
                    a.classList.add('active');
                }
                
                a.addEventListener('click', (e) => {
                    e.preventDefault();
                    navigateTo(node.path);
                });
                
                li.appendChild(a);
                parentElement.appendChild(li);
                
                if (node.type === 'folder' && node.children) {
                    const ul = document.createElement('ul');
                    node.children.forEach(child => {
                        renderTree(child, ul);
                    });
                    li.appendChild(ul);
                }
            };
            
            renderTree(directoryStructure, directoryTree);
        }

        // Render the current directory content
        function renderCurrentDirectory() {
            fileGrid.innerHTML = '';
            
            // Add "New Folder" button
            const newFolderItem = createFileItem({
                name: "New Folder",
                type: "folder",
                isAction: true,
                icon: "➕",
                action: "new-folder"
            });
            fileGrid.appendChild(newFolderItem);
            
            // Add "Upload File" button
            const uploadFileItem = createFileItem({
                name: "Upload File",
                type: "file",
                isAction: true,
                icon: "⬆️",
                action: "upload-file"
            });
            fileGrid.appendChild(uploadFileItem);
            
            // Get current directory contents
            const contents = getDirectoryContents(currentPath);
            
            if (contents && contents.length > 0) {
                contents.forEach(item => {
                    const fileItem = createFileItem(item);
                    fileGrid.appendChild(fileItem);
                });
            } else {
                const emptyMsg = document.createElement('div');
                emptyMsg.textContent = "This folder is empty";
                emptyMsg.style.gridColumn = "1 / -1";
                emptyMsg.style.textAlign = "center";
                emptyMsg.style.color = "#999";
                fileGrid.appendChild(emptyMsg);
            }
            
            // Update item count
            itemCount.textContent = `${contents ? contents.length : 0} items`;
        }

        // Create a file/folder item element
        function createFileItem(item) {
            const fileItem = document.createElement('div');
            fileItem.className = 'file-item';
            
            const fileIcon = document.createElement('div');
            fileIcon.className = 'file-icon';
            
            const fileName = document.createElement('div');
            fileName.className = 'file-name';
            
            const fileActions = document.createElement('div');
            fileActions.className = 'file-actions';
            
            if (item.isAction) {
                // Special action item (New Folder, Upload File)
                fileIcon.textContent = item.icon;
                fileName.textContent = item.name;
                fileItem.addEventListener('click', () => handleFileAction(item.action));
            } else {
                // Regular file/folder item
                fileIcon.textContent = item.type === 'folder' ? '📁' : getFileIcon(item.name);
                fileName.textContent = item.name;
                
                // Add action buttons
                const deleteBtn = document.createElement('button');
                deleteBtn.className = 'action-btn';
                deleteBtn.innerHTML = '🗑️';
                deleteBtn.title = 'Delete';
                deleteBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    deleteFile(item.path);
                });
                
                const renameBtn = document.createElement('button');
                renameBtn.className = 'action-btn';
                renameBtn.innerHTML = '✏️';
                renameBtn.title = 'Rename';
                renameBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    renameFile(item.path);
                });
                
                fileActions.appendChild(renameBtn);
                fileActions.appendChild(deleteBtn);
                
                // Navigate to folder or preview file
                if (item.type === 'folder') {
                    fileItem.addEventListener('click', () => navigateTo(item.path));
                } else {
                    fileItem.addEventListener('click', () => previewFile(item.path));
                }
            }
            
            fileItem.appendChild(fileIcon);
            fileItem.appendChild(fileName);
            fileItem.appendChild(fileActions);
            
            return fileItem;
        }

        // Get appropriate icon for file type
        function getFileIcon(filename) {
            const extension = filename.split('.').pop().toLowerCase();
            const icons = {
                'jpg': '🖼️',
                'jpeg': '🖼️',
                'png': '🖼️',
                'gif': '🖼️',
                'doc': '📄',
                'docx': '📄',
                'xls': '📊',
                'xlsx': '📊',
                'ppt': '📊',
                'pptx': '📊',
                'pdf': '📕',
                'txt': '📝',
                'html': '🌐',
                'css': '🎨',
                'js': '📜',
                'zip': '🗜️',
                'exe': '⚙️'
            };
            return icons[extension] || '📄';
        }

        // Render breadcrumb navigation
        function renderBreadcrumb() {
            breadcrumb.innerHTML = '';
            
            const parts = currentPath.split('/').filter(part => part !== '');
            let accumulatedPath = '';
            
            // Add Home link
            const homeLink = document.createElement('a');
            homeLink.href = '#';
            homeLink.textContent = 'Home';
            homeLink.setAttribute('data-path', '');
            homeLink.addEventListener('click', (e) => {
                e.preventDefault();
                navigateTo('');
            });
            breadcrumb.appendChild(homeLink);
            
            // Add path segments
            parts.forEach(part => {
                accumulatedPath += (accumulatedPath ? '/' : '') + part;
                
                const separator = document.createElement('span');
                separator.className = 'separator';
                separator.textContent = ' / ';
                breadcrumb.appendChild(separator);
                
                const link = document.createElement('a');
                link.href = '#';
                link.textContent = part;
                link.setAttribute('data-path', accumulatedPath);
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    navigateTo(accumulatedPath);
                });
                breadcrumb.appendChild(link);
            });
        }

        // Render AI suggestions
        function renderAiSuggestions() {
            suggestionsContainer.innerHTML = '';
            
            aiSuggestions.forEach(suggestion => {
                const suggestionElement = document.createElement('div');
                suggestionElement.className = 'suggestion-item';
                suggestionElement.innerHTML = `
                    <h4>${suggestion.title}</h4>
                    <p>${suggestion.description}</p>
                `;
                suggestionElement.addEventListener('click', () => handleSuggestion(suggestion.action));
                suggestionsContainer.appendChild(suggestionElement);
            });
        }

        // Navigate to a specific path
        function navigateTo(path) {
            currentPath = path;
            currentDirectory = findDirectory(path);
            renderDirectoryTree();
            renderCurrentDirectory();
            renderBreadcrumb();
            updateStatus(`Navigated to ${path || 'root'}`);
        }

        // Find directory by path
        function findDirectory(path) {
            if (!path) return directoryStructure;
            
            const parts = path.split('/');
            let current = directoryStructure;
            
            for (const part of parts) {
                if (current.children) {
                    const found = current.children.find(child => child.name === part);
                    if (found) {
                        current = found;
                    } else {
                        return null;
                    }
                } else {
                    return null;
                }
            }
            
            return current;
        }

        // Get contents of a directory
        function getDirectoryContents(path) {
            const dir = findDirectory(path);
            return dir ? dir.children : null;
        }

        // Handle file actions (new folder, upload, etc.)
        function handleFileAction(action) {
            switch (action) {
                case 'new-folder':
                    showModal('new-folder-modal');
                    break;
                case 'upload-file':
                    showModal('upload-file-modal');
                    break;
                default:
                    break;
            }
        }

        // Handle AI suggestions
        function handleSuggestion(action) {
            switch (action) {
                case 'organize':
                    updateStatus("AI is organizing your files by project...");
                    setTimeout(() => {
                        updateStatus("Files organized successfully");
                        // In a real app, this would actually organize files
                    }, 2000);
                    break;
                case 'backup':
                    updateStatus("AI is preparing backup of old files...");
                    setTimeout(() => {
                        updateStatus("Backup ready for download");
                        // In a real app, this would create a backup
                    }, 2000);
                    break;
                case 'cleanup':
                    updateStatus("AI is scanning for duplicate files...");
                    setTimeout(() => {
                        updateStatus("Found 3 duplicate files ready for review");
                        // In a real app, this would find duplicates
                    }, 2000);
                    break;
                default:
                    break;
            }
        }

        // Preview a file (simulated)
        function previewFile(path) {
            updateStatus(`Previewing file: ${path}`);
            // In a real app, this would open a preview or download the file
        }

        // Delete a file (simulated)
        function deleteFile(path) {
            if (confirm(`Are you sure you want to delete ${path}?`)) {
                updateStatus(`Deleting file: ${path}...`);
                setTimeout(() => {
                    updateStatus(`Deleted: ${path}`);
                    // In a real app, this would actually delete the file
                }, 1000);
            }
        }

        // Rename a file (simulated)
        function renameFile(path) {
            const newName = prompt("Enter new name:", path.split('/').pop());
            if (newName) {
                updateStatus(`Renaming ${path} to ${newName}...`);
                setTimeout(() => {
                    updateStatus(`Renamed to ${newName}`);
                    // In a real app, this would actually rename the file
                }, 1000);
            }
        }

        // Show modal dialog
        function showModal(modalId) {
            const modal = document.getElementById(modalId);
            modal.style.display = 'flex';
            
            const closeBtns = modal.querySelectorAll('.close-btn');
            closeBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    modal.style.display = 'none';
                });
            });
        }

        // Update status message
        function updateStatus(message) {
            statusMessage.textContent = message;
        }

        // Setup event listeners
        function setupEventListeners() {
            // Search functionality
            searchInput.addEventListener('input', handleSearch);
            
            // Create new folder
            document.getElementById('create-folder-btn').addEventListener('click', () => {
                const folderName = document.getElementById('folder-name').value.trim();
                if (folderName) {
                    updateStatus(`Creating folder: ${folderName}...`);
                    document.getElementById('new-folder-modal').style.display = 'none';
                    document.getElementById('folder-name').value = '';
                    setTimeout(() => {
                        updateStatus(`Created folder: ${folderName}`);
                        // In a real app, this would actually create the folder
                    }, 1000);
                }
            });
            
            // Upload file
            document.getElementById('upload-file-btn').addEventListener('click', () => {
                const fileInput = document.getElementById('file-upload');
                if (fileInput.files.length > 0) {
                    const fileName = fileInput.files[0].name;
                    updateStatus(`Uploading file: ${fileName}...`);
                    document.getElementById('upload-file-modal').style.display = 'none';
                    fileInput.value = '';
                    setTimeout(() => {
                        updateStatus(`Uploaded: ${fileName}`);
                        // In a real app, this would actually upload the file
                    }, 1500);
                }
            });
        }

        // Handle search input
        function handleSearch() {
            const query = searchInput.value.trim().toLowerCase();
            
            if (query.length === 0) {
                searchResults.style.display = 'none';
                return;
            }
            
            // Simulate AI search with delay
            setTimeout(() => {
                const results = searchFiles(query);
                displaySearchResults(results);
            }, 300);
        }

        // Search files in the directory structure
        function searchFiles(query) {
            const results = [];
            
            // Check if query looks like a natural language question
            const isQuestion = query.endsWith('?') || 
                               query.startsWith('how') || 
                               query.startsWith('what') || 
                               query.startsWith('where');
            
            if (isQuestion) {
                // Return AI-generated answer
                return [{
                    type: 'ai-response',
                    title: 'AI Response',
                    content: `Based on your question "${query}", I found that you have 3 project files, 5 images, and 2 documents that might be relevant. Would you like me to organize them?`,
                    action: 'organize'
                }];
            }
            
            // Regular file search
            const searchNode = (node) => {
                if (node.name.toLowerCase().includes(query)) {
                    results.push({
                        name: node.name,
                        path: node.path,
                        type: node.type
                    });
                }
                
                if (node.children) {
                    node.children.forEach(child => searchNode(child));
                }
            };
            
            searchNode(directoryStructure);
            
            return results;
        }

        // Display search results
        function displaySearchResults(results) {
            searchResults.innerHTML = '';
            
            if (results.length === 0) {
                const noResults = document.createElement('div');
                noResults.className = 'search-result-item';
                noResults.textContent = 'No results found';
                searchResults.appendChild(noResults);
            } else {
                results.forEach(result => {
                    if (result.type === 'ai-response') {
                        const aiResult = document.createElement('div');
                        aiResult.className = 'search-result-item';
                        aiResult.innerHTML = `
                            <strong>${result.title}</strong>
                            <p>${result.content}</p>
                        `;
                        aiResult.addEventListener('click', () => {
                            handleSuggestion(result.action);
                            searchInput.value = '';
                            searchResults.style.display = 'none';
                        });
                        searchResults.appendChild(aiResult);
                    } else {
                        const resultItem = document.createElement('div');
                        resultItem.className = 'search-result-item';
                        resultItem.innerHTML = `
                            <div>${result.type === 'folder' ? '📁' : '📄'} ${result.name}</div>
                            <div class="path">${result.path}</div>
                        `;
                        resultItem.addEventListener('click', () => {
                            navigateTo(result.path);
                            searchInput.value = '';
                            searchResults.style.display = 'none';
                        });
                        searchResults.appendChild(resultItem);
                    }
                });
            }
            
            searchResults.style.display = 'block';
        }

        // Initialize the app
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>
