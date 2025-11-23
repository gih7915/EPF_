<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPF - {{title or 'Plataforma Educacional'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">
                <a href="/">EPF - Plataforma Educacional</a>
            </div>
            <ul class="nav-menu">
                <li><a href="/">Home</a></li>
                <li><a href="/users">Alunos</a></li>
                <li><a href="/profs">Professores</a></li>
                <li><a href="/videoaulas?aluno_id=1">Videoaulas</a></li>
                <li><a href="/tarefas?aluno_id=1">Tarefas</a></li>
                <li><a href="/login">Login</a></li>
            </ul>
        </div>
    </nav>

    <div class="container">
        {{!base}}  <!-- O conteúdo das páginas filhas virá aqui -->
    </div>

    <footer>
        <p>&copy; 2025, EPF - Plataforma Educacional. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
