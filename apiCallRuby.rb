require 'net/http'
require 'json'


puts 'Please choose a pokemon:'

Pokemon = gets

url = 'https://pokeapi.co/api/v2/pokemon/' + Pokemon 

uri = URI.parse(URI.encode(url.strip))

res = Net::HTTP.get(uri)
puts "The result of you search is: \n"
resJ= JSON.parse(res)

puts resJ