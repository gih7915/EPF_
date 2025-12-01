% rebase('layout', title='Meu Perfil', nav_dict=nav_dict)

<div class="titulo">
    <h1>Meu Perfil</h1>
    <p>Verifique suas informações</p>
</div>

<div class="card">
    <div class="card-header">
        <div>
            <h3 class="card-title">Minhas Informações</h3>
        </div>
    </div>
    <div class="card-body">
        <p><strong>Nome:</strong> {{aluno.name}}
        <button class="open-modal" id="openModal" modal-id="nome">✏️</button></p>
        <p><strong>Matrícula:</strong> {{aluno.matricula}}
        <button class="open-modal" id="openModal" modal-id="matrícula">✏️</button></p>
        <p><strong>Email:</strong> {{aluno.email}}
        <button class="open-modal" id="openModal" modal-id="email">✏️</button></p>
    </div>
</div>

<div class="modal" id="nome">
    <div class="modal-inner">
        <form action="/meu_perfil" method="post" class="form-container">
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="matrícula">
    <div class="modal-inner">
        <form action="/meu_perfil" method="post" class="form-container">
            <div class="form-group">
                <label for="matricula">Matrícula:</label>
                <input type="text" id="matricula" name="matricula" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="email">
    <div class="modal-inner">
        <form action="/meu_perfil" method="post" class="form-container">
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>