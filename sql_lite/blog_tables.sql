-- Домашнее задание по SQL №45
-- Часть 1: Проектирование базы данных

-- Таблица 1 posts
CREATE TABLE IF NOT EXISTS posts (  
    post_id INTEGER PRIMARY KEY,
    title          INTEGER,  
    content        TEXT,  
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    slug           TEXT UNIQUE,  
    views          INTEGER DEFAULT 0,  
    category_id    INTEGER,  
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
);


-- Таблица 2 categories
CREATE TABLE IF NOT EXISTS categories (  
    category_id INTEGER PRIMARY KEY,
    name        TEXT UNIQUE  
);


-- Таблица 3 tags
CREATE TABLE IF NOT EXISTS tags (  
    tag_id INTEGER PRIMARY KEY,
    name   TEXT UNIQUE  
);


-- Таблица 4 post_tags
CREATE TABLE IF NOT EXISTS post_tags (  
    post_id         INTEGER,
    tag_id          INTEGER,  
    PRIMARY KEY (post_id, tag_id),  
    FOREIGN KEY (post_id) REFERENCES posts (post_id),
    FOREIGN KEY (tag_id) REFERENCES tags (tag_id)
);


