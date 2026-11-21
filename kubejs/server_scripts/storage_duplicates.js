// Filipovo Bombovo 2 – duplicitní úložné bedny a pytle (2026-11-21)
// Problém: víc modů má blok "9 kusů -> bedna" ze stejné suroviny. Na pracovním stole vybírá Polymorph,
// ale lis a mechanický crafter z Create (auto-compacting) vezmou vždy první recept -> náhodná bedna.
// Řešení:
//  - Vanilla suroviny (mrkev, brambory, řepa, jablko, chorus, dřevěné uhlí, sůl): zůstává jedna bedna,
//    ostatním se odebere jen recept na výrobu. Recepty "bedna -> 9 kusů" zůstávají, takže už vyrobené
//    bedny jde dál rozbalit a bloky ve světě fungují.
//  - Suroviny, které má každý mod vlastní (kukuřice, chilli, káva): bedna bere jen surovinu svého modu.
// Analýza: tools/refdata/crafting_conflicts.tsv

ServerEvents.recipes(event => {

  // ===== Zůstává: Farmer's Delight (mrkev, brambory, řepa), Fruits Delight (jablko),
  //       Ender's Delight (chorus), Mekanism (dřevěné uhlí, sůl) =====
  const removeCompress = [
    // Quark
    'quark:building/crafting/compressed/carrot_crate',
    'quark:building/crafting/compressed/potato_crate',
    'quark:building/crafting/compressed/beetroot_crate',
    'quark:building/crafting/compressed/apple_crate',
    'quark:building/crafting/compressed/chorus_fruit_block',
    'quark:building/crafting/compressed/charcoal_block',
    // Farm & Charm (pytle)
    'farm_and_charm:carrot_bag',
    'farm_and_charm:potato_bag',
    'farm_and_charm:beetroot_bag',
    // Vinery (pytel jablek)
    'vinery:apple_bag',
    // End's Delight (bedna chorusu)
    'ends_delight:chorus_fruit_crate',
    // Cultural Delights (blok soli – Mekanism bere všechny soli přes #c:dusts/salt)
    'culturaldelights:salt_block',
  ]
  removeCompress.forEach(id => event.remove({ id: id }))

  // ===== Vlastní surovina modu =====
  // Kukuřice: každý mod má vlastní klas
  event.replaceInput({ id: 'corn_delight:corn_crate' }, '#c:crops/corn', 'corn_delight:corn')
  event.replaceInput({ id: 'culturaldelights:corn_cob_crate' }, '#c:crops/corn', 'culturaldelights:corn_cob')
  // Chilli: Expanded Delight má vlastní recept z chilli_pepper
  event.replaceInput({ id: 'extradelight:chili_to_block' }, '#c:crops/chili', 'extradelight:chili')
  // Káva: #c:crops/coffee obsahuje i zrna Farmer's Respite
  event.replaceInput({ id: 'extradelight:coffee_cherries_to_block' }, '#c:crops/coffee', 'extradelight:coffee_cherries')
  event.replaceInput({ id: 'extradelight:coffee_beans_to_block' }, '#c:crops/coffee/cooked', 'extradelight:coffee_beans')
})
