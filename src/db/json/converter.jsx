const fs = require('fs')

const pokefile = JSON.parse(fs.readFileSync('./pokedex.json'));
const pokedex = pokefile;
const pokemonlist = [];
const namelist = [];
pokedex.forEach((poke) => {
    const id = poke.id;
    const im = poke.image.hires;

    const en = {name: poke.name.english, lang: "English", pokemon_id: id};
    const enf = {name: poke.name.english, lang: "English/Français", pokemon_id: id};
    const fr = {name: poke.name.french, lang:"Français", pokemon_id: id};
    const jp = {name: poke.name.japanese, lang: "日本語 (Japanese)", pokemon_id: id};
    const ch = {name: poke.name.chinese, lang: "中国人 (Chinese)", pokemon_id: id};
    const tx = poke.description;

    const pocketmon = {id:id, image: im || '', description: tx}
    pokemonlist.push(pocketmon);
    if(en.name==fr.name) {
        namelist.push(enf);
    } else {
        namelist.push(en);
        namelist.push(fr);
    }
    namelist.push(jp);
    namelist.push(ch);

});
fs.writeFile('names.json', JSON.stringify(namelist), ['utf8'], function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
}); 
fs.writeFile('pokemon.json', JSON.stringify(pokemonlist), ['utf8'], function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
}); 